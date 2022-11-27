create table if not exists users(
    id int primary key,
    name varchar(50),
    surname varchar(50),
    age int
);

insert into public.users (id, name, surname, age) values (1, 'aristotle'::varchar, 'socrates'::varchar, 100000);

