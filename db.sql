SET AUTOCOMMIT = ON

CREATE DATABASE ecommerce;

CREATE TABLE users (
    id serial primary key,
    name varchar(100),
    phone varchar(11),
    address text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);

CREATE TABLE products (
    id serial primary key,
    name text,
    description text,
    stock int,
    price int,
    version int,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);

CREATE TABLE orders (
    id serial primary key, 
    order_sn varchar(50),
    user_id int,
    total_amount int,
    status varchar(50),    
    payment_status varchar(50), 
    payment_method varchar(50),
    cancel_by varchar(50),
    cancel_reason text,
    payment_at timestamp without time zone,
    created_at timestamp without time zone,
    cancelled_at timestamp without time zone,
    updated_at timestamp without time zone
);

CREATE TABLE detail_order (
    id serial primary key,
    order_id int,
    product_id int,
    quantity int,
    sub_total int
);