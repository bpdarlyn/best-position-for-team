# These data are: 2022-01-26 16:06

current_position_table = {
    # Team, PJ, DGs, PTs
    'Brasil': (13, 23, 35),
    'Argentina': (13, 14, 29),
    'Ecuador': (14, 10, 23),
    'Colombia': (14, -1, 17),
    'Peru': (14, -5, 17),
    'Chile': (14, -1, 16),
    'Uruguay': (14, -7, 16),
    'Bolivia': (14, -8, 15),
    'Paraguay': (14, -9, 13),
    'Venezuela': (14, -16, 7),
}

next_matches = (
    # Match, Team vs Team
    (15, ('Ecuador', 'Brasil')),
    (15, ('Paraguay', 'Uruguay')),
    (15, ('Chile', 'Argentina')),
    (15, ('Colombia', 'Peru')),
    (15, ('Venezuela', 'Bolivia')),
    (16, ('Bolivia', 'Chile')),
    (16, ('Uruguay', 'Venezuela')),
    (16, ('Argentina', 'Colombia')),
    (16, ('Brasil', 'Paraguay')),
    (16, ('Peru', 'Ecuador')),
    (17, ('Argentina', 'Venezuela')),
    (17, ('Colombia', 'Bolivia')),
    (17, ('Paraguay', 'Ecuador')),
    (17, ('Brasil', 'Chile')),
    (17, ('Uruguay', 'Peru')),
    (18, ('Peru', 'Paraguay')),
    (18, ('Ecuador', 'Argentina')),
    (18, ('Venezuela', 'Colombia')),
    (18, ('Chile', 'Uruguay')),
    (18, ('Bolivia', 'Brasil')),
)

# EMPATAR, GANAR, PERDER
possible_results = (0, 1, 2)


def find_by_team(team_a, team_b, teams):
    for team in teams:
        if (team[0] == team_a and team[1] == team_b) or (team[0] == team_b and team[1] == team_a):
            r = team
            break
    else:
        r = None
    return r


def remove_duplicate_team(team_matches):
    unique = []
    for team_match in team_matches:
        team_a, team_b, _ = team_match
        if find_by_team(team_a, team_b, unique) is None:
            unique.append(team_match)
    return unique


def play_matches(team_to_verify, teams, original_position_table, total_matches, comb=[], best_table_positions=[]):
    if len(comb) == total_matches:
        # Ya jugaron todos ?
        new_table_position = build_table_position(original_position_table, comb)
        before_position_team_to_verify = list(original_position_table.keys()).index(team_to_verify)
        after_position_team_to_verify = list(new_table_position.keys()).index(team_to_verify)

        if after_position_team_to_verify <= before_position_team_to_verify:
            if not exist_table_position(new_table_position, best_table_positions):
                best_table_positions.append({
                    'matches': comb.copy(),
                    'table_positions': new_table_position.copy()
                })
        return
    i = 0
    while i < len(teams):
        current_team_match = teams[i]
        team_a, team_b, _ = current_team_match
        if current_team_match not in comb and find_by_team(team_a, team_b, comb) is None:
            comb.append(current_team_match)
            play_matches(team_to_verify, teams, original_position_table, total_matches, comb)
            team_match = comb.pop()
            comb = remove_duplicate_team(comb)

        i += 1
    return best_table_positions


def build_table_position(start_position, results):
    new_table_position = start_position.copy()
    for r in results:
        team_a, team_b, result = r
        values_team_a = new_table_position.get(team_a)
        values_team_b = new_table_position.get(team_b)
        acu_pts_a = values_team_a[-1]
        acu_pts_b = values_team_b[-1]
        if result == 0:
            # Empate
            acu_pts_a += 1
            acu_pts_b += 1
        if result == 1:
            # Gana Team A
            acu_pts_a += 3
        if result == 2:
            # Gana Team B
            acu_pts_b += 3

        new_table_position[team_a] = (values_team_a[0], values_team_a[1], acu_pts_a)
        new_table_position[team_b] = (values_team_b[0], values_team_b[1], acu_pts_b)

    return order_position_table(new_table_position)


def has_team_and_pts(team, pts, table_position):
    r = True
    for current_team, current_info in table_position.items():
        if team == current_team and pts == current_info[-1]:
            break
    else:
        r = False
    return r


def exist_table_position(table_position, table_positions):
    r = False
    for current_table_position in table_positions:
        for current_team, current_info in current_table_position['table_positions'].items():
            if not has_team_and_pts(current_team, current_info[-1], table_position):
                break
        else:
            r = True

    return r


def evaluate_team(team_to_verify, original_position_table, matches, results):
    group_match = group_next_matches_by_day(matches)
    position_table = original_position_table.copy()
    for match_day, team_matches in group_match.items():
        group_with_result = group_and_order_by_result(team_matches, results)
        best_table_positions = play_matches(team_to_verify, group_with_result, position_table, len(team_matches))
        current_position_index = list(position_table.keys()).index(team_to_verify)
        match_results = None
        for current_table_position in best_table_positions:
            simulated_position_index = list(current_table_position['table_positions'].keys()).index(team_to_verify)
            if simulated_position_index <= current_position_index:
                # Find the best position for team_to_verify
                position_table = current_table_position['table_positions']
                match_results = current_table_position['matches']

        simulated_position_index = list(position_table.keys()).index(team_to_verify)

        print(build_msg_for_match(match_day, match_results, simulated_position_index + 1, team_to_verify))


def build_msg_for_match(match, match_results, position, team):
    msg = f"Jornada {match} \n"
    msg += f"{team} queda en Posición {position}\n"
    table_msg = ""
    for mr in match_results:
        win_msg = "Empate " if mr[-1] == 0 else f"Gana {mr[0]}" if mr[-1] == 1 else f"Gana {mr[1]}"
        tmp_msg = f"{mr[0]}-{mr[1]}: {win_msg}"
        table_msg += tmp_msg + "\n"

    if table_msg != "":
        return msg + table_msg
    return 'No hay Posibilidades'


def group_next_matches_by_day(rows_next_matches):
    new_group = {}
    for row in rows_next_matches:
        # build group key
        group_key = row[0]
        # check if is a new group
        if group_key not in new_group:
            new_group[group_key] = []
        # add fare
        new_group[group_key].append(row[1])
    # return groups
    return new_group


def order_position_table(position_table):
    sorted_values = sorted(position_table.items(), key=lambda x: x[1][2], reverse=True)
    return dict(sorted_values)


def group_and_order_by_result(team_matches, results):
    new_teams = list()
    for team_match in team_matches:
        for r in results:
            value = (team_match[0], team_match[1], r)
            new_teams.append(value)
    sorted_values = sorted(new_teams, key=lambda x: x[-1])
    return list(sorted_values)


if __name__ == "__main__":
    team_to_verify = 'Bolivia'
    initial_position_table = current_position_table.copy()
    if team_to_verify in initial_position_table:
        matches = next_matches
        evaluate_team(team_to_verify=team_to_verify,
                      matches=matches,
                      original_position_table=initial_position_table,
                      results=possible_results
                      )
    else:
        print(f'{team_to_verify} is not Permitted, only is permitted')
        print(" \n".join(list(initial_position_table.keys())))
