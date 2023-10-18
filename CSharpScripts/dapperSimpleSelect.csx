#r "nuget: MySqlConnector, 2.2.7"
#r "nuget: Dapper, 2.1.11"

using Dapper;
using MySqlConnector;

record user(string id,string name,string email,string phone){
    public user():this(default,default,default,default){}
}

using (var db=new MySqlConnection("Server=127.0.0.1;Database=n;Uid=a;Pwd=a31813141;")){
    var users=db.Query<user>("select * from user");
    foreach (var user in users)
    {
        Console.WriteLine(user);
    }
    
    db.Query<user>("select * from user where id=@id",new{id=4}).ToList().ForEach(u=>Console.WriteLine(u));
}