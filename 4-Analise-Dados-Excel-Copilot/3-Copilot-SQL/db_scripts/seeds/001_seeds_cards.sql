-- First, insert the collection set (assuming this card belongs to a set)
INSERT INTO tbl_collections (
    collection_set_name,
    release_date,
    total_cards_in_collection
) VALUES (
    'Trainer Gallery',
    '2022-01-01',   -- Example release date, adjust if needed
    30              -- Example total cards in collection, adjust if needed
);

-- Then, insert the card itself
INSERT INTO tbl_cards (
    hp,
    name,
    type,
    stage,
    info,
    attack,
    damage,
    weak,
    resis,
    retreat,
    card_number_in_collection,
    collection_id
) VALUES (
    170,
    'Charizard',
    'Fire',
    'Stage 2',
    'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.',
    'Royal Blaze',
    '100+ (does 50 more damage for each Leon card in your discard pile)',
    'Water ×2',
    NULL,
    '3',
    'TG03/TG30',
    1   -- Assuming the collection inserted above has ID = 1
);
