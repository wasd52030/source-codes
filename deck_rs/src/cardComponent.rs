#[derive(Debug, strum_macros::EnumIter, Clone, Copy)]
pub enum Face {
    Hearts,
    Diamonds,
    Clubs,
    Spades,
}

impl std::fmt::Display for Face {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

#[derive(Debug, strum_macros::EnumIter, Clone, Copy)]
pub enum Suit {
    Ace,
    Due,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack,
    Queen,
    King,
}

impl std::fmt::Display for Suit {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}
