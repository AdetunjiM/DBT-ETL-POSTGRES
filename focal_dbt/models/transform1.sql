{{ config(materialized='table') }}


with emp as (
    select *
from {{source('private','employee')}}
)

select department , avg(salary) as avg_salary
from emp 
group by department