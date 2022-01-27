# Best Positions
Imagine that you have a favorite team, and you want to know until wich
position your team can reach

With this algorithm you can see all best positions for a Team.

# Requirements
- You need filled the position table dictionary
- You need filled the next matches list

By default, we are using qatar 2022 playoffs
All default data have info of `2022-01-26 16:06`

### Position Tables
```python
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
```


### Next Matches
```python
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
```


# Usage

`python3 index.py`

If you want check another team you need change the variable
that is inside `__name__` condition

```python
team_to_verify = 'Colombia'
```


**response**
```python
Jornada 15 
Bolivia queda en Posición 6
Ecuador-Brasil: Gana Brasil
Paraguay-Uruguay: Gana Uruguay
Chile-Argentina: Gana Argentina
Colombia-Peru: Gana Peru
Venezuela-Bolivia: Gana Bolivia

Jornada 16 
Bolivia queda en Posición 4
Bolivia-Chile: Gana Bolivia
Uruguay-Venezuela: Gana Venezuela
Argentina-Colombia: Gana Colombia
Brasil-Paraguay: Gana Paraguay
Peru-Ecuador: Gana Ecuador

Jornada 17 
Bolivia queda en Posición 4
Argentina-Venezuela: Gana Venezuela
Colombia-Bolivia: Gana Bolivia
Paraguay-Ecuador: Gana Ecuador
Brasil-Chile: Gana Chile
Uruguay-Peru: Gana Peru

Jornada 18 
Bolivia queda en Posición 4
Peru-Paraguay: Gana Paraguay
Ecuador-Argentina: Gana Argentina
Venezuela-Colombia: Gana Colombia
Chile-Uruguay: Gana Uruguay
Bolivia-Brasil: Gana Brasil
```



# Contributors
Feel free to usage this algorithm and if you want improvement something or comment please create an issue
or create a pull request.


# Improvements
- add to every `matches list` the probabilities that has a team A to win another Team B 
