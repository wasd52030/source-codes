using System.Linq.Expressions;

var a=new A();
a.a=4;
a.b=5;

Console.WriteLine($"field before modify -- A class {a.b}");
modifyFieldValue(ref a.b,29);
Console.WriteLine($"field after modify -- A class {a.b}");

Console.WriteLine($"Prop before modify -- A class {a.a}");
modifyPropValue(a=>a.a,a,6);
Console.WriteLine($"Prop before modify -- A class {a.a}");

void modifyFieldValue<T>(ref T field,T newvalue){
    field=newvalue;
}

void modifyPropValue<TClass,Tprop>(Expression<Func<TClass,Tprop>> expression,TClass target,Tprop newValue){
    var body=(MemberExpression)expression.Body;
    var prop=(PropertyInfo)body.Member;
    prop.GetSetMethod()!.Invoke(target,new object?[]{newValue});
}

class A{
    public int a{get;set;}
    public int b;
}
