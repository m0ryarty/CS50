--The "INSERTS" below create conditions for queries to a specific game:
--Coritiba 2 X Santos 1, from the 1985 Brazilian Championship.
--This legendary game, decided in a dramatic way at the last minute, requires this data to search for the various details of the match.
INSERT INTO address (street, number, complement, zip_code, city)
    VALUES ('Rua Ubaldino do Amaral', 37, 'Alto da Glória',  80060195, 2878 )

-
INSERT INTO stadiums (name, nickname, address)
    VALUES('Major Antônio Couto Pereira', 'Alto da Gloria - Couto Pereira', 1)


INSERT INTO teams (name, short_name, colors, symbol, foundation, nickname, mascot, stadium, address)
    VALUES('Coritiba Foot Ball Club', 'Coritiba', 'Green and White', 'https://www.coritiba.com.br/imgs/logo.png', '1909-10-12', 'Coxa Branca', 'Vovô Coxa', 1, 1)


    
INSERT INTO address (street, number, complement, zip_code, city)
    VALUES ('Rua Princesa Isabel', NULL, 'Vila Belmiro', 11075500, 5250)

INSERT INTO stadiums (name, nickname, address)
    VALUES('Urbano Caldeira','Vila Belmiro', 2)

INSERT INTO teams (name, short_name,  colors, symbol, foundation, nickname, mascot, stadium, address)
    VALUES('Santos Futebol Clube', 'Santos', 'Black and White', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Santos_Logo.png/120px-Santos_Logo.png', '1912-04-14', 'Peixe', 'Baleia', 2, 2)


INSERT INTO championships (name, year)
    VALUES('Campeonato Brasileiro', 1985)


INSERT INTO games (datetime, home_team, visitor_team, stadium, championship)
    VALUES ('1985-04-14', 1, 2, 1, 1)


INSERT INTO players (nickname)
    VALUES 
        ('Rafael'),
        ('André'), 
        ('Gomes'), 
        ('Vavá'), 
        ('Dida'), 
        ('Almir'), 
        ('Marco Aurélio'), 
        ('Tobi'), 
        ('Lela'), 
        ('Índio'), 
        ('Édson'),
        ('Marolla'), 
        ('Paulo Roberto'), 
        ('Márcio Rossini'), 
        ('Toninho Carlos'),
        ('Paulo Róbson'), 
        ('Dema'), 
        ('Humberto'), 
        ('Formiga'), 
        ('Gallo'),         
        ('Lima'), 
        ('Zé Sérgio'),
        ('Vicente'),
        ('Gersinho')



INSERT INTO line_ups (game, team, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11)
    VALUES(1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

INSERT INTO line_ups (game, team, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11)
    VALUES(1, 2, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)


INSERT INTO substitutions (game, team, player_in, player_out)
    VALUES
        (1, 1, 23, 11),
        (1, 2, 24, 20)


INSERT INTO goals (scorer, game, team, time, period)
    VALUES
        (4, 1, 1, '00:25', 'first'),
        (14, 1, 2, '00:29', 'first'),
        (9, 1, 1, '00:45', 'second')


INSERT INTO country (id, name, name_pt, acronym) 
    VALUES
        (1, 'Brazil', 'Brasil', 'BR')

--After this, it is possible to make queries and obtain details of the match.
--Who scored the match:
SELECT player_nickname, team_short_name, time, period FROM game_goals
    WHERE home = 'Coritiba'
    AND  visitor = 'Santos'
    AND championship = 'Campeonato Brasileiro'
    AND year = 1985       
    ORDER BY period;
   
                
--The final score:
SELECT team_short_name, COUNT(team_short_name) FROM game_goals
    WHERE home = 'Coritiba'
    AND  visitor = 'Santos' 
    AND championship = 'Campeonato Brasileiro'
    AND year = 1985           
    GROUP BY team_short_name

-- Team details of tha match:
SELECT
team,
short_name, 
colors, 
foundation, 
mascot,
symbol,
nickname,
stadium, 
city, 
state,
country, 
street,
number,
zip_code
FROM teams_details
    WHERE short_name = 'Santos'

-- The line ups:
SELECT team, player11, 
home
FROM game_line_up
    WHERE visitor = 'Santos'
    AND championship = 'Campeonato Brasileiro'
    AND year = 1985