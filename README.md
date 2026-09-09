# POS Inventory Service

A transactional retail domain service by **Varun Madala** for products, stock, and sales. It prevents overselling, validates inputs, records each sale, and updates inventory in one database transaction.

## Run tests

```bash
python -m unittest -v
```

The domain layer can sit behind REST, gRPC, a desktop POS client, or a legacy XML adapter. SQLite makes the project immediately runnable; SQL Server is the intended production substitute.

## Author

Varun Madala

