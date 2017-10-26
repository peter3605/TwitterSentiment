use project;
drop table tweet_info;
create table tweet_info(
	tweet_id varchar(100),
    username varchar(100),
    creation_date varchar(100),
    text varchar(500),
    is_text_positive varchar(1),
    sentiment_score decimal(40,30)
);