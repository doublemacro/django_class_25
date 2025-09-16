
text = """If I were to begin by giving a full and consistent case history, it would
place the reader in a very different situation from that of the medical
observer. The reports of the patient’s relatives – in the present case I was
given one by the eighteen-year-old girl’s father – usually afford a very
indistinct picture of the course of the illness. I begin the treatment,
indeed, by asking the patient to give me the whole story of his life and
illness, but even so the information I receive is never enough to let me
see my way about the case. This first account may be compared to an
unnavigable
river whose stream is at one moment choked by masses of
rock and at another divided and lost among shallows and sandbanks. I
cannot help wondering how it is that the authorities can produce such
smooth and precise histories in cases of hysteria. As a matter of fact the
patients are incapable of giving such reports about themselves. They can,
indeed, give the physician plenty of coherent information about this or
that period of their lives; but it is sure to be followed by another period
as to which their communications run dry, leaving gaps unfilled, and riddles
unanswered; and then again will come yet another period which
will remain totally obscure and unilluminated by even a single piece of
serviceable information. The connections – even the ostensible ones –
are for the most part incoherent, and the sequence of different events is
uncertain. Even during the course of their story patients will repeatedly
correct a particular or a date, and then perhaps, after wavering for some
time, return to their first version. The patients’ inability to give an
ordered history of their life insofar as it coincides with the history of
their illness is not merely characteristic of the neurosis.2 It also possesses great theoretical significance. For this inability has the following
grounds. In the first place, patients consciously and intentionally keep
back part of what they ought to tell – things that are perfectly well
known to them – because they have not got over their feelings T
of timidity and shame (or discretion, where what they say concerns other
people); this is the share taken by conscious disingenuousness. In the
second place, part of the anamnestic knowledge, which the patients have
at their disposal at other times, disappears while they are actually telling
their story, but without their making any deliberate reservations: the
share taken by unconscious disingenuousness. In the third place, there
are invariably true amnesias – gaps in the memory into which not only
old recollections but even quite recent ones have fallen – and paramnesias,
formed secondarily so as to fill in those gaps.1 When the events
themselves have been kept in mind, the purpose underlying the amnesias
can be fulfilled just as surely by destroying a connection, and a connection
is most surely broken by altering the chronological order of events.
The latter always proves to be the most vulnerable element in the store of
memory and the one which is most easily subject to repression. Again, we
meet with many recollections that are in what might be described as the
first stage of repression, and these we find surrounded with doubts. At a
later period the doubts would be replaced by a loss T or a
falsification of memory.
That this state of affairs should exist in regard to the memories
relating to the history of the illness is a necessary correlate of the symptoms
and one which is theoretically requisite. In the further course of the
treatment the patient supplies the facts which, though he had known
them all along, had been kept back by him or had not occurred to his
mind . The paramnesias prove untenable, and the gaps in his
memory are filled in. It is only towards the end of the treatment that we
have before us an intelligible, consistent and unbroken case history.
Whereas the practical aim of the treatment is to remove all possible
symptoms and to replace them with conscious thoughts, we may regard it
as a second and theoretical aim to repair all the damages to the patient’s"""

cerinte="""
Creati o clasa TextProcessor, care implementeaza urmatoarele metode:
- word_count(text), care returneaza un dictionar cu fiecare cuvant, si de cate ori se gaseste in text. Cuvinta cu 2 sau mai multe caractere. Exemplu:
{
  "query": 2,
  "this": 5,
  "the": 10,
  "cat": 2,
}
- top_common_words(text, top_count), care returneaza un dictionar cu cuvintele care se regasesc cel mai des in text.
- unique_words(text), care returneaza o lista cu cuvinte unice, care se gasesc o singura data in text.
- short_words(text), care returneaza o lista de cuvinte cu 3 litere sau mai putin.
- capitalized_count(text), care primeste un text, si numara cate cuvinte sunt scrise cu litera mare.
- text_word_count(text), care numara toate cuvintele din text, mai lungi de 2 cifre.
- sorted_even_words(text), care returneaza o lista de cuvinte sortate alfabetic, fiecare cuvant are un numar par de litere.
- inverse_sorted_odd_words(text), care returneaza o lista de cuvinte sortate invers alfabetic, fiecare cuvant cu numar impar de litere.

Ignorati spatiile, cuvintele cu o litera, si semnele de punctuatie pentru toate functiile de mai sus, incluzand si numere.

Si functiile urmatoare:
- get_capitalized(text), care returneaza o lista de cuvinte capitalizate.
- contains_letter(text, letter), care returneaza toate cuvintele care contin litera data.
- cleanup(text), care returneaza o lista de cuvinte, toate cuvintele cu 2 litere sau mai mult, fara spatii, punctuatii.
- letter_limit_words(text, count), care returneaza cuvintele cu nr de litere pus in "count".

Si inlantuiti-le una dupa alta. Adica primiti un text, apelati cleanup(text), si dupa ce returneaza cleanup(text), apelati de exemplu letter_limit_words(cleanup(text), 3).
"""

# exemplu, nu e corect implementat nimic.
class TextProcessor:
    def word_count(self, text):
        word_list = text.split(" ")
        return word_list

processor = TextProcessor()
processor.word_count(text)
