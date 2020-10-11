


create table information(
	info_id varchar2(64), -- 
	info_title varchar2(64),
	info_img varchar2(64),
	info_url varchar2(64),
	info_tag varchar2(64)
)

create table live_streaming(
	live_id varchar2(64),
	live_title varchar2(64),
	live_img varchar2(64),
	live_tag varchar2(64)
)

create table info_live_relationship(
	info_id varchar2(64),
	live_id varchar2(64)
)

create table live_calendar(
	live_id varchar2(64),
	live_title varchar2(64),
	live_start_time varchar2(64),
	live_url varchar2(64),
	live_img varchar2(64), -- 没有的话，前端随机显示e小宝。
	live_tag varchar2(64)
)
