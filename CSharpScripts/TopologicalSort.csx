// reference -> https://www.bilibili.com/video/BV1Kc411Q751
IEnumerable<T> TopologicalSort<T>(IDictionary<T, ISet<T>> garph) where T:IComparable<T>
{
    var count_dict = garph.ToDictionary(k => k.Key, v => 0);
    var queue = new Queue<T>();
    var res = new List<T>();

    foreach (var item in garph)
    {
        foreach (var child in item.Value)
        {
            count_dict[child]++;
        }
    }

    foreach (var item in count_dict)
    {
        if (item.Value == 0)
        {
            queue.Enqueue(item.Key);
        }
    }

    // while queue is non-empty do
    while (queue.Any())
    {
        var n = queue.Dequeue();
        res.Add(n);
        var child_set = garph[n];
        foreach (var child in child_set)
        {
            count_dict[child]--;
            if (count_dict[child] == 0)
            {
                queue.Enqueue(child);
            }
        }
    }

    return res;
}


var garph = new Dictionary<int, ISet<int>>(){
    {1,new HashSet<int>(){2,3}},
    {2,new HashSet<int>(){4}},
    {3,new HashSet<int>(){4}},
    {4,new HashSet<int>(){5}},
    {5,new HashSet<int>(){}}
};

Console.WriteLine($"[{string.Join(",", TopologicalSort(garph))}]");
