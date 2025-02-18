- **BASIC**
    - SELECT : select * from db_name.table_name
    - FILTERING:
        - [`WHERE`](https://datalemur.com/sql-tutorial/sql-where) allows us to filter rows based on specified conditions
        - [`AND and OR`](https://datalemur.com/sql-tutorial/sql-and-or-not) allow you to combine multiple filtering conditions
        - [`BETWEEN`](https://datalemur.com/sql-tutorial/sql-between) allows you to filter on a range of values
        - [`IN`](https://datalemur.com/sql-tutorial/sql-in) allows you to specify a list of values that you'd like to filter on
        - [`LIKE`](https://datalemur.com/sql-tutorial/sql-like-wildcard-pattern) allows you to match a value against a pattern
        
        Here's a comprehensive table of the different operators you can use in conjunction with `WHERE` to filter your data:
        
        | **Operator** | **Definition** | **Example in Query** | **Interpretation** |
        | --- | --- | --- | --- |
        | = | Equals to | `user_id = 2` | user_id is equal to 2 |
        | !=, <> | Not equals to | `user_id != 5` | user_id is not equal to 5 |
        | <, > | Less than, more than | `age < 5` | age is less than 5 |
        | <=, >= | Less than or equal to, more than or equal to | `age >= 2` | age is equal to or greater than 2 |
        | BETWEEN … AND … | Integer is within range of two values (inclusive) | `pushups BETWEEN 20 AND 40` | pushups is between 20 and 40 (inclusive) |
        | IN (…) | Value is in a list | `first_name IN ('Bob', 'Ann', 'Joe')` | first name is either Bob, Ann, or Joe |
        | LIKE | Checks if a string matches a pattern | `first_name LIKE 'Jo%` | first name starts with "Jo" |
    - SORTING:
        - ORDER BY

---

- **JOINS**
    
    ### 1. **Inner Join**
    
    - **Definition**: Returns rows when there is a match in both tables.
    - **Use Case**: When you need data that exists in both tables.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table1 a
        INNER JOIN table2 b ON a.common_field = b.common_field;
        
        ```
        
    - **Example**: Find employees and their department names if they have been assigned to a department.
    
    ### 2. **Left (Outer) Join**
    
    - **Definition**: Returns all rows from the left table and matched rows from the right table. If no match, NULLs are returned for columns from the right table.
    - **Use Case**: When you need all data from the left table, with relevant matches (or lack thereof) from the right table.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table1 a
        LEFT JOIN table2 b ON a.common_field = b.common_field;
        
        ```
        
    - **Example**: Get all employees and their department names; include employees without a department.
    
    ### 3. **Right (Outer) Join**
    
    - **Definition**: Returns all rows from the right table and matched rows from the left table. If no match, NULLs are returned for columns from the left table.
    - **Use Case**: When you need all data from the right table, regardless of matching rows in the left table.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table1 a
        RIGHT JOIN table2 b ON a.common_field = b.common_field;
        
        ```
        
    - **Example**: Find all departments and employees who belong to those departments; include departments without employees.
    
    ### 4. **Full (Outer) Join**
    
    - **Definition**: Combines the result of both left and right joins. Returns all rows when there is a match in either table; unmatched rows will have NULLs.
    - **Use Case**: When you need all data from both tables, regardless of matching.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table1 a
        FULL OUTER JOIN table2 b ON a.common_field = b.common_field;
        
        ```
        
    - **Example**: List all employees and departments, including those without matches.
    
    ### 5. **Cross Join**
    
    - **Definition**: Returns the Cartesian product of both tables (all combinations of rows).
    - **Use Case**: When you need every possible combination of rows between two tables.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table1 a
        CROSS JOIN table2 b;
        
        ```
        
    - **Example**: Pair each product with every customer for a marketing analysis.
    
    ### 6. **Self Join**
    
    - **Definition**: A join where a table is joined with itself.
    - **Use Case**: When you need to compare rows within the same table.
    - **Syntax**:
        
        ```sql
        SELECT a.column1, b.column2
        FROM table a, table b
        WHERE a.some_field = b.some_field;
        
        ```
        
    - **Example**: Find employees who have the same manager.
    
    ### 7. **Key Points to Remember**
    
    - **Performance**: Joins can be resource-intensive; optimize with indexes.
    - **NULLs**: Be mindful of NULLs, especially in outer joins.
    - **ON vs WHERE**: `ON` is used to specify join conditions; `WHERE` filters results after the join.
    - **Check Duplicates**: Cartesian products (cross joins) may lead to unintended duplicates.
    - **Combine Joins**: Sometimes you may need nested joins for complex queries.

---

- **CASE-WHEN (IF ELSE IN SQL)**
    
    ### `CASE` Statement in PostgreSQL (Conditional Logic)
    
    ### 1. **Definition**:
    
    - The `CASE` statement is used to implement conditional logic within SQL queries. It acts like an `if-else` statement.
    
    ### 2. **Syntax**:
    
    ```sql
    SELECT
      column1,
      CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ELSE result_default
      END AS alias_name
    FROM table_name;
    
    ```
    
    ### 3. **Examples**:
    
    - **Example 1: Categorizing Data**
        
        ```sql
        SELECT
          employee_name,
          salary,
          CASE
            WHEN salary > 80000 THEN 'High'
            WHEN salary BETWEEN 50000 AND 80000 THEN 'Medium'
            ELSE 'Low'
          END AS salary_category
        FROM employees;
        
        ```
        
        - **Explanation**: Classifies employees into 'High', 'Medium', or 'Low' salary categories based on their salary.
    - **Example 2: Simple Conditional Update**
        
        ```sql
        SELECT
          order_id,
          order_date,
          CASE delivery_status
            WHEN 'Delivered' THEN 'Completed'
            WHEN 'Pending' THEN 'In Progress'
            ELSE 'Unknown'
          END AS status_label
        FROM orders;
        
        ```
        
        - **Explanation**: Maps delivery statuses to custom labels.
    
    ### 4. **Key Points**:
    
    - **WHEN** clause: Specifies the condition to evaluate.
    - **THEN** clause: Result returned if the condition is true.
    - **ELSE** clause: Default result if none of the `WHEN` conditions are met.
    - The `CASE` statement ends with `END`.
    - The `CASE` statement can be used in `SELECT`, `UPDATE`, `ORDER BY`, and `WHERE` clauses.
    
    ### 5. **Nested CASE Statements**:
    
    - You can nest `CASE` statements for more complex logic:
        
        ```sql
        SELECT
          employee_id,
          CASE
            WHEN department = 'HR' THEN
              CASE
                WHEN experience > 5 THEN 'Senior HR'
                ELSE 'Junior HR'
              END
            ELSE 'Other Department'
          END AS position
        FROM employees;
        
        ```
        
    
    ### 6. **Using `CASE` in `UPDATE`**:
    
    - To update a column based on conditions:
        
        ```sql
        UPDATE employees
        SET job_title =
          CASE
            WHEN department = 'Sales' THEN 'Sales Manager'
            WHEN department = 'IT' THEN 'IT Specialist'
            ELSE 'General Staff'
          END;
        
        ```
        
    
    ### 7. **Practical Uses**:
    
    - **Data Transformation**: Transform column values for easier reading.
    - **Conditional Aggregation**: Use in `GROUP BY` and `HAVING` for tailored result sets.
        - **Scenario**: Calculate the total sales categorized by regions and only include results where sales exceed a certain threshold for specific conditions.
            - **Example**:
                
                ```sql
                SELECT
                  region,
                  SUM(
                    CASE
                      WHEN product_type = 'Electronics' THEN sales_amount
                      ELSE 0
                    END
                  ) AS total_electronics_sales
                FROM sales
                GROUP BY region
                HAVING SUM(
                  CASE
                    WHEN product_type = 'Electronics' THEN sales_amount
                    ELSE 0
                  END
                ) > 100000;
                
                ```
                
                - **Explanation**: The `CASE` statement inside the `SUM` function aggregates sales only for the 'Electronics' category. The `HAVING` clause ensures only regions where total sales of 'Electronics' exceed 100,000 are included.
    - **Complex Filters**: Combine logic in `WHERE` clauses.
        - **Scenario**: Select orders where specific conditions apply, such as different status labels for `order_status`.
        - **Example**:
            
            ```sql
            SELECT
              order_id,
              customer_name,
              order_date
            FROM orders
            WHERE
              CASE
                WHEN delivery_status = 'Shipped' AND delivery_date IS NULL THEN FALSE
                WHEN order_status = 'Cancelled' THEN FALSE
                ELSE TRUE
              END;
            
            ```
            
            - **Explanation**: This query filters out orders that are 'Shipped' but have no delivery date, and also excludes cancelled orders. The `CASE` statement in the `WHERE` clause enables conditional logic to apply complex filtering based on multiple conditions.

---
