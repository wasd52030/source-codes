import java.util.Collections
import kotlin.random.Random
 
enum class Face {
    Hearts, Diamonds, Clubs, Spades
}
 
enum class Suit {
    Ace, Due, Three, Four, Five, Six,
    Seven, Eight, Nine, Ten, Jack, Queen, King
}
 
class Card(f: Face, s: Suit) {
    private var face = f
    private var suit = s
 
 
    override fun toString(): String {
        return "$face-$suit"
    }
}
 
 
class Deck {
 
    private var data = arrayListOf<Card>()
    private var currentCard = 0;
 
    init {
        for (f in Face.values()) {
            for (s in Suit.values()) {
                data.add(Card(f, s))
            }
        }
    }
 
    public fun getCardnums(): Int {
        return data.size
    }
 
    public fun shuffle() {
        for (x in 0 until data.size) {
            val y = Random.nextInt(data.size)
 
            Collections.swap(data, x, y)
        }
    }
 
    public fun draw(): Card {
        if (data.size > 0) {
            return data.removeAt(0)
        }
        throw Error("No Cards in Deck")
    }
}
 
 
fun main() {
    var d = Deck()
    d.shuffle()
    for (i in 0 until d.getCardnums()) {
        println(d.draw())
    }
}
