DROP TABLE IF EXISTS pass ;

CREATE TABLE pass 
	(
	id serial primary key,
	word text,
	count int
	);

CREATE TABLE users
	(
	userid serial primary key,
	email text,
	firstname text,
	lastname text,
	password text
	);

CREATE TABLE userpass
	(
	uniqid serial primary key,
	userid int,
	password text,
	FOREIGN KEY (userid) REFERENCES users(userid)
	);

ALTER TABLE pass ADD CONSTRAINT pass_word_key UNIQUE (word);

CREATE INDEX word_idx on pass USING btree (word);
CREATE INDEX user_idx on users USING btree (email);