@startuml 货币兑换系统ER图
!define Table(name, desc) class name as "**Table: name**\\n----\\n desc" {
  +id : BIGINT (PK)
}

Table(customers, "客户信息表") {
  +full_name : VARCHAR(100)
  +email : VARCHAR(100) UNIQUE
  +phone : VARCHAR(20) UNIQUE
  +id_card_no : VARCHAR(20) UNIQUE
  +total_transaction_count : INT
  +total_exchange_volume : DECIMAL(15,2)
  +status : ENUM('ACTIVE','FROZEN')
  +created_at : DATETIME
  +updated_at : DATETIME
}

Table(currencies, "货币基础表") {
  +currency_code : VARCHAR(3) UNIQUE (PK)
  +currency_name : VARCHAR(50)
  +symbol : VARCHAR(5)
  +decimal_places : TINYINT
  +is_base_currency : BOOLEAN
  +is_active : BOOLEAN
}

Table(exchange_rates, "汇率表") {
  +id : BIGINT (PK)
  +base_currency_code : VARCHAR(3) (FK -> currencies)
  +target_currency_code : VARCHAR(3) (FK -> currencies)
  +buy_rate : DECIMAL(10,6)
  +sell_rate : DECIMAL(10,6)
  +mid_rate : DECIMAL(10,6)
  +effective_date : DATE
  +expiry_date : DATE
  +source : VARCHAR(50)
}

Table(transactions, "交易流水表") {
  +id : BIGINT (PK)
  +transaction_no : VARCHAR(50) UNIQUE
  +customer_id : BIGINT (FK -> customers)
  +base_currency_code : VARCHAR(3) (FK -> currencies)
  +target_currency_code : VARCHAR(3) (FK -> currencies)
  +base_amount : DECIMAL(15,2)
  +target_amount : DECIMAL(15,2)
  +exchange_rate_used : DECIMAL(10,6)
  +transaction_type : ENUM('BUY','SELL')
  +status : ENUM('PENDING','SUCCESS','FAILED','REFUNDED')
  +fee_amount : DECIMAL(15,2)
  +fee_currency_code : VARCHAR(3)
  +completed_at : DATETIME
  +created_at : DATETIME
}

Table(currency_inventory, "货币库存表") {
  +currency_code : VARCHAR(3) (PK, FK -> currencies)
  +available_balance : DECIMAL(15,2)
  +locked_balance : DECIMAL(15,2)
  +reorder_threshold : DECIMAL(15,2)
  +last_updated : DATETIME
}

' ---------- 关系定义 ----------
customers ||--o{ transactions : "发起"
currencies ||--o{ exchange_rates : "作为基础货币"
currencies ||--o{ exchange_rates : "作为目标货币"
currencies ||--o{ transactions : "作为基础货币"
currencies ||--o{ transactions : "作为目标货币"
currencies |o--|| currency_inventory : "库存"

@enduml