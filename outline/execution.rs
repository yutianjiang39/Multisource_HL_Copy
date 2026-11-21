//! Outline only: turning events into execution results.
//!
//! This file only explains what the execution part of Multisource HL Copy is
//! responsible for. The production engine is private, and the names here are
//! illustrative, not a callable public API. Bodies are `unimplemented!`
//! ("实现未公开") on purpose; nothing here pretends to place or fill orders.

/// Something the engine learns about: a source or own-account event, or loss of a feed.
pub enum Event {
    SourceOrder { source: SourceId, coin: String },
    SourceFill { source: SourceId, coin: String },
    OwnUpdate { coin: String },
    FeedGap,
}

pub struct SourceId(pub u32);

/// What the engine decides to do. Every add goes through admission first.
pub enum Action {
    MirrorResting,
    AmendPrice,
    CancelMirror,
    FollowTakerOpen,
    FollowReduce,
    CleanupResidual,
    PauseAdds,
}

/// The only three ways a sent request can end. Unknown is never resent.
pub enum Outcome {
    NotSent,
    Confirmed,
    Unknown,
}

/// Per-coin ownership across sources: one owner at a time, first come first served.
pub trait Ownership {
    fn owner_of(&self, coin: &str) -> Option<SourceId>;
}

/// Admission: identity claim, risk ledger and permits before anything is sent.
pub trait Admission {
    fn admit(&mut self, event: &Event) -> Option<Action>;
}

pub struct Engine;

impl Engine {
    pub fn handle(&mut self, _event: Event) -> Vec<Action> {
        unimplemented!("实现未公开")
    }

    pub fn settle(&mut self, _action: &Action) -> Outcome {
        unimplemented!("实现未公开")
    }
}
