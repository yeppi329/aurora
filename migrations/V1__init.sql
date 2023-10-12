create table IF NOT EXISTS user_active_history
(
    active_history_idx bigserial
        primary key,
    active_user_id     varchar                                            not null,
    active_dt          varchar                                            not null,
    created_at         timestamp with time zone default CURRENT_TIMESTAMP not null,
    unique(active_user_id, active_dt)
);

comment on table user_active_history is '활성 이용자 히스토리 테이블';

comment on column user_active_history.active_history_idx is '활성 이용자 히스토리 고유값';
comment on column user_active_history.active_user_id is '사용자 고유값';
comment on column user_active_history.active_dt is '활성일자(YYYY-MM-DD)';
comment on column user_active_history.created_at is '배치 일시';

alter table user_active_history
    owner to postgres;