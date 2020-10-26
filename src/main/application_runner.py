# Created by Leon Hunter at 8:29 PM 10/25/2020
from src.main.mysql_configurator import MySqlConfigurator

if __name__ == "__main__":
  database_name = "my_database_name"
  table_name = "my_table_name"
  mysql_configurator = MySqlConfigurator(database_name)

  create_table = '''
  CREATE TABLE IF NOT EXISTS {}.{}(
  	id int auto_increment primary key,
  	name text not null,
  	primary_type int not null,
  	secondary_type int null);
  '''.format(database_name, table_name)

  insert_into_table = '''
  INSERT INTO {}.{} 
  (id, name, primary_type, secondary_type) 
   VALUES (12, 'Ivysaur', 3, 7);
  '''.format(database_name, table_name)

  mysql_configurator.drop()
  mysql_configurator.create()
  mysql_configurator.use()
  mysql_configurator.execute(create_table)
  mysql_configurator.execute(insert_into_table)