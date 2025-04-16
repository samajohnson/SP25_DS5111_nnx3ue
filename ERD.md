erDiagram
    STOCKS {
        string symbol PK
        date date PK
        float open
        float high
        float low
        float close
        int volume
    }

    RECURRING_STOCKS {
        string symbol PK
        int occurrences
        string occurrence_dates
    }
 
    VOLATILE_STOCKS {
        string symbol PK
        float max_intraday_change
        float avg_intraday_change
        float max_weekly_change
        float avg_weekly_change
    }

    STEADY_STOCKS {
        string symbol PK
        float min_intraday_change
        float avg_intraday_change
        float min_weekly_change
        float avg_weekly_change
    }

    PRICE_RANGES {
        string symbol PK
        date date PK
        float daily_range
        float weekly_range
    }

    VOLUME_RANGES {
        string symbol PK
        date date PK
        int daily_volume_change
        int weekly_volume_change
    }

    STOCKS ||--o{ RECURRING_STOCKS : "feeds"
    STOCKS ||--o{ VOLATILE_STOCKS : "feeds"
    STOCKS ||--o{ STEADY_STOCKS : "feeds"
    STOCKS ||--o{ PRICE_RANGES : "feeds"
    STOCKS ||--o{ VOLUME_RANGES : "feeds"
