-- Check if the user already exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

-- Create the user if it does not exist
SET @create_user_query = IF(@user_exists = 0, 
                            'CREATE USER \'user_0d_1\'@\'localhost\' IDENTIFIED BY \'user_0d_1_pwd\';', 
                            'SELECT \'User already exists\' status;');
PREPARE stmt FROM @create_user_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Grant privileges only if the user was just created
SET @grant_privileges_query = IF(@user_exists = 0,
                                 'GRANT ALL PRIVILEGES ON *.* TO \'user_0d_1\'@\'localhost\'; FLUSH PRIVILEGES;', 
                                 'SELECT \'User already had privileges\' status;');
PREPARE stmt FROM @grant_privileges_query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

