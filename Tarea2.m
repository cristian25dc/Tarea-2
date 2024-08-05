pkg load database %cargar el paquete

conn=pq_connect(setdbopts('dbname','test','host','localhost','port','5432','user','postgres','password','edcamey2020'))

N=pq_exec_params(conn, "insert into redes values('Carlos, 201400524');")%insertar datos en la tabla

N=pq_params(conn, 'select * from redes;')%ver datos en la tabla
