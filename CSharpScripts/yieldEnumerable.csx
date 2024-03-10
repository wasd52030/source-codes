IEnumerable<double> s() {
    while (true) {
        Console.Write("score: ");
        double.TryParse(Console.ReadLine(),out double x);
        if (x==-1) {
            yield break;
        }
        else {
            yield return x;
        }
    }
}

var u=s().ToList();
Console.WriteLine(u.Count());
Console.WriteLine($"{u.Sum()} {u.Sum()/u.Count()}");