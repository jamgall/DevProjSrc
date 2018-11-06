DROP TABLE IF EXISTS pass ;

CREATE TABLE pass 
	(
	id serial primary key,
	word text
	);

ALTER TABLE pass ADD CONSTRAINT pass_word_key UNIQUE (word);

CREATE INDEX word_idx on pass USING btree (word);
