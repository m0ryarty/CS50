-- Active: 1731664534680@@127.0.0.1@5432@footballdb
-- In this SQL file, write (and comment!) the schema of your database, including the CREATE TABLE, CREATE INDEX, CREATE VIEW, etc. statements that compose it

CREATE DATABASE 
    footballdb

-- Teams details. The team has an address and can have a stadium.
CREATE TABLE IF NOT EXISTS teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    short_name VARCHAR(25) NOT NULL,
    colors VARCHAR(255) NOT NULL,
    symbol VARCHAR NOT NULL,
    foundation DATE NOT NULL,
    nickname VARCHAR(255) NOT NULL,
    mascot VARCHAR(255),
    stadium INTEGER,
    address INTEGER
)

-- The stadiums where are played the games. May or may not belong to a team 
CREATE TABLE IF NOT EXISTS stadiums (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),        
    address INTEGER    
)

-- Goals are scored by one player, on one team and in one game.
CREATE TABLE IF NOT EXISTS goals (
    id SERIAL PRIMARY KEY,
    scorer INTEGER,
    game INTEGER,
    team INTEGER,
    time TIME,
    period VARCHAR(20) CHECK (period = 'first' or period = 'second' or period = 'extra-first' or period = 'extra-second' or period = 'penalty')
    )

--The game will take place in a stadium. There will be a visiting team and a home team.
CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    datetime Date,
    home_team INTEGER,
    visitor_team INTEGER,
    stadium INTEGER,
    championship INTEGER,
    attendance INTEGER,
    video VARCHAR(50)    
)

--A team's lineup has 11 players, belongs to one team and refers to one game.
CREATE TABLE IF NOT EXISTS line_ups (
    id SERIAL PRIMARY KEY,
    game INTEGER,
    team INTEGER,
    player1 INTEGER,
    player2 INTEGER,
    player3 INTEGER,
    player4 INTEGER,
    player5 INTEGER,
    player6 INTEGER,
    player7 INTEGER,
    player8 INTEGER,
    player9 INTEGER,
    player10 INTEGER,
    player11 INTEGER
)

--Substitutions occur in a game by having one player come in and another player go out.
CREATE TABLE IF NOT EXISTS substitutions (
    id SERIAL PRIMARY KEY,
    game INTEGER,
    team INTEGER,
    player_out INTEGER,
    player_in INTEGER,
    time TIME
)

--Each championship is identified by its name and season. A championship has many games or just one..
CREATE TABLE IF NOT EXISTS championships (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year INTEGER
    
)

--A player plays for a many teams. Each player has a unique ID, name, nickname, nationality, date of birth, date of retirement, and image.
CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) ,
    nickname VARCHAR(255),
    nationality VARCHAR(255),
    birth DATE,
    retired DATE,    
    image VARCHAR
    )

--All the countries of the world.
CREATE TABLE IF NOT EXISTS country (
    id SERIAL PRIMARY KEY,    
    name VARCHAR(60),
    name_pt VARCHAR(60),
    acronym VARCHAR(2)        
)

-- Countries are divided by states, but they can be provinces, regions or other divisions depending on local reality. 
CREATE TABLE IF NOT EXISTS state (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    acronym VARCHAR(2),
    country INTEGER
    
    )

-- All the cities where football are played.
CREATE TABLE IF NOT EXISTS city (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) DEFAULT NULL,
  state INTEGER DEFAULT NULL,
  country INTEGER DEFAULT NULL    
)

--Stadiums or teams have an address. The addresses are in cities.
CREATE TABLE IF NOT EXISTS address (
    id SERIAL PRIMARY KEY,
    street VARCHAR(120) DEFAULT NULL,
    number INTEGER DEFAULT NULL,
    complement VARCHAR(120) DEFAULT NULL,
    zip_code VARCHAR(10) DEFAULT NULL,
    city INTEGER    
)

-- The foreign key are created below in every table that were references.
ALTER TABLE teams
    ADD CONSTRAINT fk_teams_stadium
    FOREIGN KEY (stadium)
    REFERENCES stadiums (id)
    ON DELETE SET NULL

ALTER TABLE teams
    ADD CONSTRAINT fk_teams_address
    FOREIGN KEY (address)
    REFERENCES address (id)
    ON DELETE SET NULL

ALTER TABLE stadiums
    ADD CONSTRAINT fk_stadiums_address
    FOREIGN KEY (address)
    REFERENCES address (id)
    ON DELETE SET NULL

ALTER TABLE goals
    ADD CONSTRAINT fk_goals_scorer
    FOREIGN KEY (scorer)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE goals
    ADD CONSTRAINT fk_goals_game
    FOREIGN KEY (game)
    REFERENCES games (id)
    ON DELETE CASCADE

ALTER TABLE goals
    ADD CONSTRAINT fk_goals_team
    FOREIGN KEY (team)
    REFERENCES teams (id)
    ON DELETE CASCADE

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_game
    FOREIGN KEY (game)
    REFERENCES games (id)
    ON DELETE CASCADE


ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_team
    FOREIGN KEY (team)
    REFERENCES teams (id)
    ON DELETE CASCADE

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player1
    FOREIGN KEY (player1)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player2
    FOREIGN KEY (player2)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player3
    FOREIGN KEY (player3)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player4
    FOREIGN KEY (player4)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player5
    FOREIGN KEY (player5)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player6
    FOREIGN KEY (player6)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player7
    FOREIGN KEY (player7)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player8
    FOREIGN KEY (player8)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player9
    FOREIGN KEY (player9)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player10
    FOREIGN KEY (player10)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE line_ups
    ADD CONSTRAINT fk_line_ups_player11
    FOREIGN KEY (player11)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE substitutions
    ADD CONSTRAINT fk_substitutions_game
    FOREIGN KEY (game)
    REFERENCES games (id)
    ON DELETE CASCADE

ALTER TABLE substitutions
    ADD CONSTRAINT fk_substitutions_team
    FOREIGN KEY (team)
    REFERENCES teams (id)
    ON DELETE CASCADE

ALTER TABLE substitutions
    ADD CONSTRAINT fk_substitutions_player_out
    FOREIGN KEY (player_out)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE substitutions
    ADD CONSTRAINT fk_substitutions_player_in
    FOREIGN KEY (player_in)
    REFERENCES players (id)
    ON DELETE SET NULL

ALTER TABLE games
    ADD CONSTRAINT fk_games_home_team
    FOREIGN KEY (home_team)
    REFERENCES teams (id)
    ON DELETE SET NULL

ALTER TABLE games
    ADD CONSTRAINT fk_games_visitor_team
    FOREIGN KEY (visitor_team)
    REFERENCES teams (id)
    ON DELETE SET NULL

ALTER TABLE games
    ADD CONSTRAINT fk_games_stadium
    FOREIGN KEY (stadium)
    REFERENCES stadiums (id)
    ON DELETE SET NULL

ALTER TABLE games
    ADD CONSTRAINT fk_games_championship
    FOREIGN KEY (championship)
    REFERENCES championships (id)
    ON DELETE SET NULL;


ALTER TABLE city
    ADD CONSTRAINT fk_city_state
    FOREIGN KEY (state)
    REFERENCES state (id)
    ON DELETE SET NULL

ALTER TABLE city
    ADD CONSTRAINT fk_city_country
    FOREIGN KEY (country)
    REFERENCES country (id)
    ON DELETE SET NULL

ALTER TABLE state
    ADD CONSTRAINT fk_state_country
    FOREIGN KEY (country)
    REFERENCES country (id)
    ON DELETE SET NULL

ALTER TABLE address
    ADD CONSTRAINT fk_address_city
    FOREIGN KEY (city)
    REFERENCES city (id)
    ON DELETE SET NULL


-- These views were created to facilitate the most common queries. 
CREATE VIEW "game_goals" AS
SELECT
 players.nickname AS player_nickname,  
 t_id.short_name AS team_short_name, 
 time, 
 period,
 t_id.id AS team_id, 
 t_h.short_name AS home, 
 t_v.short_name AS visitor, 
 championships.name AS championship,
 championships.year AS year,
 datetime AS date 
 FROM games
JOIN goals ON games.id = goals.game
JOIN championships ON championships.id = games.championship
JOIN players ON scorer = players.id
JOIN teams t_id ON t_id.id = goals.team
JOIN teams t_h ON home_team = t_h.id
JOIN teams t_v ON visitor_team = t_v.id



CREATE VIEW "teams_details" AS
SELECT 
teams.name AS team,
teams.short_name, 
colors, 
foundation, 
mascot,
symbol,
teams.nickname,
stadiums.name AS stadium, 
city.name AS city, 
state.name AS state,
country.name AS country, 
street,
number,
zip_code 
FROM teams
    JOIN address ON address = address.id
    JOIN city ON address.city = city.id
    JOIN state ON city.state = state.id
    JOIN country ON city.country = country.id
    JOIN stadiums ON stadium = stadiums.id


CREATE VIEW game_line_up AS
SELECT 
p1.nickname AS player1, 
p2.nickname AS player2,
p3.nickname AS player3, 
p4.nickname AS player4, 
p5.nickname AS player5, 
p6.nickname AS player6, 
p7.nickname AS player7, 
p8.nickname AS player8, 
p9.nickname AS player9, 
p10.nickname AS player10, 
p11.nickname AS player11,
t_id.short_name AS team,
t_h.short_name AS home,
t_v.short_name AS visitor,
championships.name AS championship,
championships.year AS year,
games.datetime AS date
FROM line_ups lu 
JOIN players p1 ON lu.player1 = p1.id 
JOIN players p2 ON lu.player2 = p2.id 
JOIN players p3 ON lu.player3 = p3.id 
JOIN players p4 ON lu.player4 = p4.id 
JOIN players p5 ON lu.player5 = p5.id 
JOIN players p6 ON lu.player6 = p6.id 
JOIN players p7 ON lu.player7 = p7.id 
JOIN players p8 ON lu.player8 = p8.id 
JOIN players p9 ON lu.player9 = p9.id 
JOIN players p10 ON lu.player10 = p10.id 
JOIN players p11 ON lu.player11 = p11.id
JOIN teams t_id ON team = t_id.id
JOIN games ON lu.game = games.id
JOIN teams t_h ON home_team = t_h.id
JOIN teams t_v ON visitor_team = t_v.id
JOIN championships ON games.championship = championships.id

-- End of SQL schema creation statements --