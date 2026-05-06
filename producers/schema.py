STOCK_TICK_SCHEMA = {
    "type": "record",
    "name": "StockTick",
    "namespace": "com.stockpipeline",
    "fields": [
        {"name": "symbol",      "type": "string"},
        {"name": "price",       "type": "double"},
        {"name": "volume",      "type": "double"},
        {"name": "timestamp",   "type": "long"},
        {"name": "vwap",        "type": ["null", "double"], "default": None},
        {"name": "trade_count", "type": ["null", "int"],    "default": None}
    ]
}