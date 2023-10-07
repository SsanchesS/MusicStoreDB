CREATE TABLE Albums(
  album_id INTEGER PRIMARY KEY,
  title TEXT,
  artist_id INTEGER,
  release_date DATE,
  genre_id INTEGER,
  FOREIGN KEY (artist_id) REFERENCES Artists (artist_id),
  FOREIGN KEY (genre_id) REFERENCES Genres (genre_id)
);
CREATE TABLE Artists(
  artist_id INTEGER PRIMARY KEY,
  name TEXT,
  country TEXT,
  active_years TEXT
); 
CREATE TABLE Genres(
  genre_id INTEGER PRIMARY KEY,
  name TEXT
  ); 
CREATE TABLE Songs(
  song_id INTEGER PRIMARY KEY,
  title TEXT,
  album_id INTEGER,
  artist_id INTEGER,
  duration TEXT,
  FOREIGN KEY (album_id) REFERENCES Albums (album_id),
  FOREIGN KEY (artist_id) REFERENCES Artists (artist_id)
); 
CREATE TABLE Customers(
  customer_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  phone_number TEXT  
);
CREATE TABLE Orders(
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  order_date DATE,
  total_amount FLOAT,
  FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
); 
CREATE TABLE OrderDetails(
  order_detail_id INTEGER PRIMARY KEY,
  order_id INTEGER,
  song_id INTEGER,
  quantity INTEGER,
  price FLOAT,
  FOREIGN KEY (order_id) REFERENCES Orders (order_id),
  FOREIGN KEY (song_id) REFERENCES Songs (song_id)
)
CREATE TABLE Employees(
  employee_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  hire_date DATE,
  position TEXT
)
CREATE TABLE Publishers(
  publisher_id INTEGER PRIMARY KEY,
  name TEXT,
  country TEXT
)
CREATE TABLE Copyrights(
  copyright_id INTEGER PRIMARY KEY,
  song_id INTEGER,
  publisher_id INTEGER,
  royalty_rate FLOAT,
  FOREIGN KEY (song_id) REFERENCES Songs (song_id),
  FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
)

-- INSERT INTO Albums (title, artist_id, release_date, genre_id) VALUES ('Road', 1, '1969-09-26', 1);
-- INSERT INTO Albums (title, artist_id, release_date, genre_id) VALUES ('Thriller', 2, '1982-11-30', 2);
-- INSERT INTO Albums (title, artist_id, release_date, genre_id) VALUES ('The LP', 3, '2000-05-23', 3);

-- INSERT INTO Artists (name, country, active_years) VALUES ('The Beat', 'UK', '1960-1970');
-- INSERT INTO Artists (name, country, active_years) VALUES ('Michael Jackson', 'USA', '1964-2009');
-- INSERT INTO Artists (name, country, active_years) VALUES ('Eminem', 'USA', '1992-2023');

-- INSERT INTO Genres (name) VALUES ('Rock');
-- INSERT INTO Genres (name) VALUES ('Pop');
-- INSERT INTO Genres (name) VALUES ('Hip-Hop');

-- INSERT INTO Songs (title, album_id, artist_id, duration) VALUES ('Come Together', 1, 1, '4:20');
-- INSERT INTO Songs (title, album_id, artist_id, duration) VALUES ('Billie Jean', 2, 2, '4:54');
-- INSERT INTO Songs (title, album_id, artist_id, duration) VALUES ('Stan', 3, 3, '6:44');

-- INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES ('John', 'Doe', 'johndoe@example.com', '+7 123-456-7890');
-- INSERT INTO Customers (first_name, last_name, email, phone_number) VALUES ('Jane', 'Smith', 'janesmith@example.com', '+7 987-654-3210');

-- INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (1, '2023-09-15', 100.0);
-- INSERT INTO Orders (customer_id, order_date, total_amount) VALUES (2, '2023-09-15', 75.5);

-- INSERT INTO OrderDetails (order_id, song_id, quantity, price) VALUES (1, 1, 2, 1.0);
-- INSERT INTO OrderDetails (order_id, song_id, quantity, price) VALUES (1, 2, 1, 1.5);
-- INSERT INTO OrderDetails (order_id, song_id, quantity, price) VALUES (2, 3, 3, 2.0);

-- INSERT INTO Employees (first_name, last_name, hire_date, position) VALUES ('Alice', 'Johnson', '2022-01-15', 'Manager');
-- INSERT INTO Employees (first_name, last_name, hire_date, position) VALUES ('Bob', 'Smith', '2022-02-20', 'Sales Associate');

-- INSERT INTO Publishers (name, country) VALUES ('Sony Music', 'USA');
-- INSERT INTO Publishers (name, country) VALUES ('Universal Music', 'USA');

-- INSERT INTO Copyrights (song_id, publisher_id, royalty_rate) VALUES (1, 1, 0.1);
-- INSERT INTO Copyrights (song_id, publisher_id, royalty_rate) VALUES (2, 2, 0.15);
-- INSERT INTO Copyrights (song_id, publisher_id, royalty_rate) VALUES (3, 1, 0.12);

-- SELECT * FROM Albums;
-- SELECT * FROM Artists;
-- SELECT * FROM Genres;
-- SELECT * FROM Songs;
-- SELECT * FROM Customers;
-- SELECT * FROM Orders;
-- SELECT * FROM OrderDetails;
-- SELECT * FROM Employees;
-- SELECT * FROM Publishers;
-- SELECT * FROM Copyrights;