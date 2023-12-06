set client_encoding = 'utf8';

create temporary table temp_award (
    institution text,
    award text,
    country_awarding text
);

\copy temp_award(institution, award, country_awarding) from 'sql/award.csv' delimiter ',' csv header;

insert into institution (name)
    select distinct institution from temp_award;

insert into award (id_institution, name, country_awarding)
    select institution.id, award, country_awarding   
    from temp_award left join institution on temp_award.institution = institution.name;

create temporary table temp_nomination (
    year int,
    award text,
    title text,
    country_submitting text
);

\copy temp_nomination(year, award, title, country_submitting) from 'sql/nomination.csv' delimiter ',' csv header;

insert into movie (title)
    select title from temp_nomination;

insert into nomination
    (year, id_award, id_movie, country_submitting)
    select year, award.id, movie.id, country_submitting
    from
        temp_nomination left join award on temp_nomination.award = award.name
        left join movie on temp_nomination.title = movie.title;

drop table temp_award, temp_nomination;
