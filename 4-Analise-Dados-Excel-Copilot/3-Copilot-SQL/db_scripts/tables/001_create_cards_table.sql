-- Create table for collection sets
CREATE TABLE tbl_collections (
    id SERIAL PRIMARY KEY,
    collection_set_name VARCHAR(255) NOT NULL,
    release_date DATE NOT NULL,
    total_cards_in_collection INT NOT NULL
);

-- Create table for Pokémon TCG cards
CREATE TABLE tbl_cards (
    id SERIAL PRIMARY KEY,
    hp INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100),
    stage VARCHAR(50),
    info TEXT,
    attack VARCHAR(255),
    damage VARCHAR(50),
    weak VARCHAR(100),
    resis VARCHAR(100),
    retreat VARCHAR(50),
    card_number_in_collection VARCHAR(50),
    collection_id INT NOT NULL,
    CONSTRAINT fk_collection
        FOREIGN KEY (collection_id) 
        REFERENCES tbl_collections (id)
        ON DELETE CASCADE
);
