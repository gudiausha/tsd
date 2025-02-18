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

- **WHERE,GROUP BY AND HAVING**
    
    ### `GROUP BY`, `HAVING`, and `WHERE` Clauses - Key Notes
    
    ### 1. **`WHERE` Clause**
    
    - **Purpose**: Filters rows before any grouping occurs.
    - **Use Case**: Applies to individual rows in a table.
    - **Syntax**:
        
        ```sql
        SELECT column1, column2
        FROM table_name
        WHERE condition;
        
        ```
        
    - **Example**:
        
        ```sql
        SELECT employee_id, department
        FROM employees
        WHERE salary > 50000;
        
        ```
        
        - **Explanation**: Selects employees with a salary greater than 50,000.
    - **Key Point**:
        - Cannot be used with aggregate functions like `SUM`, `COUNT`, etc.
        - SQL does not allow column aliases defined in the SELECT statement to be used in the WHERE clause because the WHERE clause is processed before the SELECT clause.
    
    ### 2. **`GROUP BY` Clause**
    
    - **Purpose**: Groups rows that share a common value into summary rows, typically used with aggregate functions.
    - **Use Case**: To perform aggregation on specific columns.
    - **Syntax**:
        
        ```sql
        SELECT column1, aggregate_function(column2)
        FROM table_name
        GROUP BY column1;
        
        ```
        
    - **Example**:
        
        ```sql
        SELECT department, COUNT(employee_id)
        FROM employees
        GROUP BY department;
        
        ```
        
        - **Explanation**: Counts the number of employees in each department.
    - **Key Point**: All columns in the `SELECT` statement (not used with aggregate functions) must be included in `GROUP BY`.
    - In SQL, the order of columns in a `GROUP BY` clause affects how the data is grouped and, consequently, how the results are presented. Here's a detailed look at how column order in `GROUP BY` impacts query results:
        
        ### 1. **Grouping Hierarchy**:
        
        - The columns in the `GROUP BY` clause define the grouping hierarchy. The data is grouped first by the leftmost column, then by the next column, and so on. This means that the order matters because it determines the primary, secondary, etc., levels of grouping.
        - Example:
            
            ```sql
            SELECT department, job_title, COUNT(*)
            FROM employees
            GROUP BY department, job_title;
            
            ```
            
            - In this query, the data is first grouped by `department`. Within each `department`, it is further grouped by `job_title`.
        - Swapping the column order changes the grouping:
            
            ```sql
            SELECT department, job_title, COUNT(*)
            FROM employees
            GROUP BY job_title, department;
            
            ```
            
            - Now, the data is grouped first by `job_title` and then by `department` within each `job_title`. This can lead to different results or just a different structure of aggregation.
        
        ### 2. **Impact on Results**:
        
        - The order impacts how aggregate functions are calculated and how results are structured. Changing the order might not change the overall totals but will affect the breakdown and how subtotals are grouped and displayed.
        - For example:
            - `GROUP BY department, job_title` groups by department first, showing counts per department and then per job title within that department.
            - `GROUP BY job_title, department` groups by job title first, showing counts per job title and then breaking them down by department within each job title.
        
        ### 3. **Output Presentation**:
        
        - While `GROUP BY` itself does not control the sort order of the output (that's what `ORDER BY` is for), the order of columns in `GROUP BY` affects how data is logically grouped. To ensure data appears in the same hierarchical order as `GROUP BY`, you would typically pair it with an `ORDER BY` clause using the same columns.
        
        ### Example Analysis:
        
        Suppose you have a table `sales` with columns `region`, `product`, and `sales_amount`:
        
        ```sql
        SELECT region, product, SUM(sales_amount)
        FROM sales
        GROUP BY region, product;
        
        ```
        
        - **Grouped by `region` first**: The result will show totals for each `region` and then break those totals down by `product` within each `region`.
        
        If you swap the order:
        
        ```sql
        SELECT region, product, SUM(sales_amount)
        FROM sales
        GROUP BY product, region;
        
        ```
        
        - **Grouped by `product` first**: The result will show totals for each `product` and then break those totals down by `region` within each `product`.
        
        ### Summary:
        
        - **Order matters in `GROUP BY` because it determines the grouping hierarchy**.
        - **Results can be different in structure**, impacting how aggregate functions are calculated for different groupings.
        - **Choose the order based on your desired data presentation** and the logical structure you need for analysis.
    
    ### 3. **`HAVING` Clause**
    
    - **Purpose**: Filters groups after the grouping is done. Used to apply conditions to aggregate functions.
    - **Use Case**: Acts like a `WHERE` clause but for aggregated/grouped data.
    - **Syntax**:
        
        ```sql
        SELECT column1, aggregate_function(column2)
        FROM table_name
        GROUP BY column1
        HAVING aggregate_function(column2) condition;
        
        ```
        
    - **Example**:
        
        ```sql
        SELECT department, AVG(salary)
        FROM employees
        GROUP BY department
        HAVING AVG(salary) > 60000;
        
        ```
        
        - **Explanation**: Returns departments where the average salary is greater than 60,000.
    - **Key Point**: Must be used after `GROUP BY`.
    
    ### 4. **When and Where to Use Each**:
    
    - **`WHERE`**:
        - **When**: Before grouping, to filter rows based on conditions.
        - **Where**: Used before `GROUP BY` in the query.
    - **`GROUP BY`**:
        - **When**: When aggregation of data based on columns is needed.
        - **Where**: Placed after the `WHERE` clause and before `HAVING`.
    - **`HAVING`**:
        - **When**: To filter grouped data or aggregated results.
        - **Where**: Always after `GROUP BY`.
    
    ### 5. **Example Query Combining All**:
    
    ```sql
    SELECT department, COUNT(employee_id) AS total_employees
    FROM employees
    WHERE is_active = TRUE
    GROUP BY department
    HAVING COUNT(employee_id) > 5;
    
    ```
    
    - **Explanation**:
        - **`WHERE is_active = TRUE`**: Filters only active employees.
        - **`GROUP BY department`**: Groups by department.
        - **`HAVING COUNT(employee_id) > 5`**: Ensures only departments with more than 5 employees are shown.
    
    ### 6. **Order of Execution**:
    
    1. **`WHERE`** filters rows.
    2. **`GROUP BY`** groups rows.
    3. **Aggregate Functions** (e.g., `SUM`, `AVG`, `COUNT`) are applied.
    4. **`HAVING`** filters grouped results.

---

- **AGGREGATE FUNCTIONS**
    
    Aggregate functions in PostgreSQL are used to compute a single result from a set of input values. These functions are commonly used with the `GROUP BY` clause to group rows based on one or more columns and perform aggregate calculations on those groups.
    
    ### 1. **Common Aggregate Functions**
    
    - **`COUNT()`**: Returns the number of input rows that match a specific condition.
        
        ```sql
        SELECT COUNT(*) FROM employees;
        
        ```
        
    - **`SUM()`**: Calculates the total sum of a numeric column.
        
        ```sql
        SELECT department, SUM(salary) FROM employees GROUP BY department;
        
        ```
        
    - **`AVG()`**: Returns the average value of a numeric column.
        
        ```sql
        SELECT department, AVG(salary) FROM employees GROUP BY department;
        
        ```
        
        - **Key Points:**
            - **NULLs are ignored** in the calculation.
            - Can be combined with `DISTINCT` to find the average of unique values.
                
                ```sql
                sql
                Copy code
                SELECT AVG(DISTINCT salary) FROM employees;
                
                ```
                
    - **`MIN()`**: Returns the minimum value in a column.
        
        ```sql
        SELECT MIN(salary) FROM employees;
        
        ```
        
    - **`MAX()`**: Returns the maximum value in a column.
        
        ```sql
        SELECT MAX(salary) FROM employees;
        
        ```
        
    - **`STRING_AGG()`**: Concatenates strings from a group into a single string, with a specified delimiter.
        
        ```sql
        SELECT department, STRING_AGG(employee_name, ', ') FROM employees GROUP BY department;
        
        ```
        
    - **`ARRAY_AGG()`**: Returns an array of the aggregated values.
        
        ```sql
        SELECT department, ARRAY_AGG(employee_id) FROM employees GROUP BY department;
        
        ```
        
    - **`ABS()`**
        - **Purpose**: The `ABS()` function returns the absolute (non-negative) value of a numeric input.
        - **Use Cases**: Useful in financial and mathematical calculations to ensure positive results.
        
        **Example**:
        
        ```sql
        sql
        Copy code
        SELECT ABS(-25.5);  -- Result: 25.5
        SELECT ABS(salary) FROM employees;
        
        ```
        
        - **Notes**: This function works on all numeric types, including integers, decimals, and floats.
    
    ### **`TO_CHAR()` Function**
    
    - **Purpose**: The `TO_CHAR()` function converts various data types (e.g., numbers, dates) into a string format with specific formatting.
    - **Use Cases**:
        - Formatting dates and times for display purposes.
        - Formatting numbers with thousands separators, currency symbols, or fixed decimal places.
    
    **Syntax**:
    
    ```sql
    sql
    Copy code
    TO_CHAR(value, format);
    
    ```
    
    **Examples**:
    
    - **Formatting Numbers**:
        
        ```sql
        sql
        Copy code
        SELECT TO_CHAR(12345.678, 'FM99999.00');  -- Result: '12345.68'
        SELECT TO_CHAR(1234567, '9,999,999');     -- Result: '1,234,567'
        
        ```
        
    - **Formatting Dates**:
        
        ```sql
        sql
        Copy code
        SELECT TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS');  -- Result: '2024-11-13 14:30:00'
        SELECT TO_CHAR(DATE '2024-11-13', 'Day, DDth Month YYYY');  -- Result: 'Wednesday, 13th November 2024'
        
        ```
        
    
    ### **Notes for `TO_CHAR()`**:
    
    - It is not an aggregate function but is often used in combination with aggregate functions to format the output.
    - Custom formats allow flexible representations using format patterns (e.g., `YYYY` for the year, `FM` to suppress leading zeros).
    
    ### 2. **Usage with `GROUP BY`**
    
    - Aggregate functions are often used with the `GROUP BY` clause to aggregate data for each group.
        
        ```sql
        SELECT department, COUNT(*), AVG(salary)
        FROM employees
        GROUP BY department;
        
        ```
        
    
    ### 3. **Usage with `HAVING`**
    
    - The `HAVING` clause filters results after aggregation. It is similar to `WHERE`, but for aggregated results.
        
        ```sql
        SELECT department, SUM(salary)
        FROM employees
        GROUP BY department
        HAVING SUM(salary) > 50000;
        
        ```
        
    
    ### 4. **Distinct Values in Aggregates**
    
    - Use `DISTINCT` to eliminate duplicate values within the aggregation.
        
        ```sql
        SELECT COUNT(DISTINCT department) FROM employees;
        
        ```
        
    
    ### 5. **Ordering Results in Aggregates**
    
    - For functions like `STRING_AGG()` or `ARRAY_AGG()`, you can specify the order of the aggregated results.
        
        ```sql
        SELECT department, STRING_AGG(employee_name, ', ' ORDER BY employee_name)
        FROM employees
        GROUP BY department;
        
        ```
        
    
    ### 6. **Advanced Usage: Window Functions**
    
    - Aggregate functions can be used with **window functions** for more complex analytical queries.
        
        ```sql
        SELECT employee_id, department, SUM(salary) OVER (PARTITION BY department)
        FROM employees;
        
        ```
        
    
    ### Key Points to Remember:
    
    - Aggregate functions ignore `NULL` values unless specified otherwise.
    - `GROUP BY` is used to group data for aggregation.
    - `HAVING` is used for filtering aggregated results.
    - Use `DISTINCT` to avoid counting duplicates.
    - Aggregates can be used in combination with window functions for advanced analysis.
    
    These aggregate functions are powerful tools for summarizing and analyzing data in PostgreSQL, making them essential for data-driven applications and reporting.

---
    
- **WINDOW FUNCTIONS**
    
    **Window functions** in PostgreSQL allow you to perform calculations across a set of table rows that are related to the current row. This makes them powerful for complex analytical queries, enabling operations like running totals, rank assignments, and moving averages without grouping rows into a single output row like aggregate functions.
    
    ### Key Concepts:
    
    - **Window**: The set of rows a function acts upon.
    - **`OVER()` Clause**: Defines the window (the rows the function operates on).
    - **Partitions**: The subset of data that the window operates on (similar to `GROUP BY` but does not reduce the result set).
    - **Order**: The sorting order within the partition, essential for functions like `RANK()` or running totals.
    
    ### 1. **Common Window Functions**
    
    - **`ROW_NUMBER()`**: Assigns a unique sequential number to each row in a result set.
        
        ```sql
        SELECT employee_id, department, salary,
               ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
        FROM employees;
        
        ```
        
    - **`RANK()`**: Similar to `ROW_NUMBER()`, but rows with equal values receive the same rank, with the next rank skipping as needed.
        
        ```sql
        SELECT employee_id, department, salary,
               RANK() OVER (ORDER BY salary DESC) AS rank
        FROM employees;
        
        ```
        
    - **`DENSE_RANK()`**: Similar to `RANK()`, but without gaps in rank values for ties.
        
        ```sql
        SELECT employee_id, department, salary,
               DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
        FROM employees;
        
        ```
        
    - **`NTILE(n)`**: Divides rows into `n` buckets and assigns a bucket number.
        
        ```sql
        SELECT employee_id, department, salary,
               NTILE(4) OVER (ORDER BY salary DESC) AS bucket
        FROM employees;
        
        ```
        
    - **`SUM()`** (with `OVER` clause): Used for running totals or cumulative sums.
        
        ```sql
        SELECT employee_id, department, salary,
               SUM(salary) OVER (PARTITION BY department ORDER BY salary) AS running_total
        FROM employees;
        
        ```
        
    - **`AVG()`**, **`MIN()`**, **`MAX()`**: Can be used similarly to calculate moving averages or sliding windows.
        
        ```sql
        SELECT employee_id, department, salary,
               AVG(salary) OVER (PARTITION BY department ORDER BY salary ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS moving_avg
        FROM employees;
        
        ```
        
    
    ### 2. **`OVER()` Clause Details**
    
    - **Basic Use**:
        
        ```sql
        SELECT employee_id, salary,
               SUM(salary) OVER () AS total_salary
        FROM employees;
        
        ```
        
    - **Partitioning**:
        
        ```sql
        SELECT department, employee_id, salary,
               SUM(salary) OVER (PARTITION BY department) AS department_total
        FROM employees;
        
        ```
        
    - **Ordering**:
        
        ```sql
        SELECT employee_id, department, salary,
               SUM(salary) OVER (ORDER BY salary DESC) AS cumulative_sum
        FROM employees;
        
        ```
        
    
    ### 3. **Frame Specification**
    
    - Defines the subset of rows within the partition that the function operates on:
        - **`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`**: Includes all rows from the start of the partition up to the current row.
        - **`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`**: Includes one row before and one row after the current row.
        - **`RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`**: Similar to `ROWS`, but considers value ranges.
    
    **Example**:
    
    ```sql
    SELECT employee_id, salary,
           SUM(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_sum
    FROM employees;
    
    ```
    
    ### Use Cases:
    
    - **Ranking**: Find top-performing employees by sales.
    - **Running Totals**: Calculate a cumulative salary sum within a department.
    - **Moving Averages**: Analyze performance trends over time.
    - **Percentiles**: Distribute employees into salary quartiles.
    
    ### Summary:
    
    Window functions enhance SQL's capability for analytical queries, providing insights into data trends and patterns without collapsing rows like traditional aggregate functions. They are crucial for business intelligence, reporting, and complex data analysis.

---

- **QUERY ORDER OF EXECUTION**
    
    Understanding the order of execution in SQL helps in writing optimized queries and debugging effectively. Here is the step-by-step execution order in SQL:
    
    1. **`FROM` Clause**
        - The first step is to identify and gather the data from the source tables.
        - Joins and subqueries in the `FROM` clause are executed at this stage.
    2. **`WHERE` Clause**
        - Filters rows based on conditions.
        - Only rows that meet the `WHERE` conditions pass to the next stage.
        - Does **not** interact with aggregate functions; operates on raw data.
    3. **`GROUP BY` Clause**
        - Groups the filtered data based on one or more columns.
        - Used to prepare data for aggregation.
    4. **`HAVING` Clause**
        - Filters groups created by `GROUP BY`.
        - Works similarly to `WHERE` but is applied after grouping, allowing aggregate functions.
    5. **`SELECT` Clause**
        - Selects columns or expressions from the data set.
        - Aliases defined here cannot be used in the `WHERE`, `GROUP BY`, or `HAVING` clauses.
    6. **`DISTINCT` Keyword**
        - Removes duplicate rows from the result set after data is selected.
        - Applied after the `SELECT` clause.
    7. **`ORDER BY` Clause**
        - Sorts the result set based on one or more columns.
        - Can use column numbers (e.g., `ORDER BY 1`) or column aliases.
    8. **`LIMIT`/`OFFSET` Clauses**
        - Limits the number of rows returned by the query or skips rows.
        - Executed last to restrict the final result set.
    
    ### Example of Order Explained:
    
    ```sql
    SELECT department, COUNT(employee_id)
    FROM employees
    WHERE salary > 50000
    GROUP BY department
    HAVING COUNT(employee_id) > 5
    ORDER BY department;
    
    ```
    
    **Execution Steps**:
    
    1. **`FROM employees`**: Loads the data from the `employees` table.
    2. **`WHERE salary > 50000`**: Filters rows where `salary` is greater than 50,000.
    3. **`GROUP BY department`**: Groups remaining rows by the `department` column.
    4. **`HAVING COUNT(employee_id) > 5`**: Filters groups where the number of employees is more than 5.
    5. **`SELECT department, COUNT(employee_id)`**: Selects the columns `department` and the count of `employee_id`.
    6. **`ORDER BY department`**: Sorts the result set by the `department` column.
    
    Understanding this logical order helps in anticipating how a query processes and returns data.