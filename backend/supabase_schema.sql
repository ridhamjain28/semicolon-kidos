-- KidOS - IBLM Schema for Supabase

-- 1. Kernels: The child's persistent "Learning Brain"
CREATE TABLE IF NOT EXISTS iblm_kernels (
    user_id TEXT PRIMARY KEY,
    age INTEGER NOT NULL,
    curiosity_type TEXT DEFAULT 'exploratory',
    mastery_levels JSONB DEFAULT '{}',
    rules JSONB DEFAULT '[]',
    last_active TIMESTAMPTZ DEFAULT now()
);

-- 2. Signals: The raw interaction logs for behavior analysis
CREATE TABLE IF NOT EXISTS iblm_signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    signal_type TEXT NOT NULL, -- e.g., "skip", "dwell", "text"
    f_score NUMERIC DEFAULT 0,  -- Frustration
    svi_score NUMERIC DEFAULT 0, -- Stimulus Value
    action_taken TEXT,
    event_type TEXT,
    timestamp TIMESTAMPTZ DEFAULT now()
);
