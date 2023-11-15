#r "nuget: Dapper, 2.1.15"
#r "nuget: MySqlConnector, 2.2.7"

using Dapper;
using MySqlConnector;

record user(string id,string name,string email,string phone){
    public user():this(default,default,default,default){}
}

using (var db=new MySqlConnection("Server=127.0.0.1;Database=n;Uid=a;Pwd=a31813141;")){
    db.Query<user>("select * from user").ToList().ForEach(Console.WriteLine);
    Console.WriteLine();
    
    db.Query<user>("select * from user where id=@id",new{id=4}).ToList().ForEach(Console.WriteLine);
}