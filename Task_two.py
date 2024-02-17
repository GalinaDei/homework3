# Задание 2
#✔ В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью  из википедии или из документации к языку.

import re
from collections import Counter

text ='''collections — Типы данных контейнеров
Исходный код: Lib/collections/__init__.py

Этот модуль реализует специализированные типы данных контейнеров, предоставляя альтернативы встроенным контейнерам общего назначения Python, dict, list, set, и tuple.

namedtuple()

заводская функция для создания подклассов кортежей с именованными полями

deque

контейнер, подобный списку, с быстрым добавлением и всплывающими окнами на обоих концах

ChainMap

подобный dict класс для создания единого представления нескольких сопоставлений

Counter

подкласс dict для подсчета хэшируемых объектов

OrderedDict

добавлен подкласс dict, который запоминает записи порядка

defaultdict

подкласс dict, вызывающий заводскую функцию для предоставления отсутствующих значений

UserDict

оболочка вокруг объектов словаря для упрощения создания подклассов dict

UserList

оболочка вокруг объектов списка для упрощения создания подклассов списка

UserString

оболочка вокруг строковых объектов для упрощения создания подклассов string

ChainMap объекты
Новое в версии 3.3.

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

The class can be used to simulate nested scopes and is useful in templating.

class collections.ChainMap(*maps)
A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

The underlying mappings are stored in a list. That list is public and can be accessed or updated using the maps attribute. There is no other state.

Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and deletions only operate on the first mapping.

A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.

All of the usual dictionary methods are supported. In addition, there is a maps attribute, a method for creating new subcontexts, and a property for accessing all but the first mapping:

maps
A user updateable list of mappings. The list is ordered from first-searched to last-searched. It is the only stored state and can be modified to change which mappings are searched. The list should always contain at least one mapping.

None=m(new_child, **kwargs)
Возвращает new ChainMap, содержащий новую карту, за которой следуют все карты в текущем экземпляре. Если m указано, оно становится новой картой в начале списка сопоставлений; если не указано, используется пустой dict , так что вызов d.new_child() эквивалентен: ChainMap({}, *d.maps). Если указаны какие-либо аргументы ключевого слова, они обновляют переданную карту или новый пустой dict . Этот метод используется для создания подтекстов, которые могут быть обновлены без изменения значений в любом из родительских отображений.

Изменено в версии 3.4: был добавлен необязательный m параметр.

Изменено в версии 3.10: добавлена поддержка аргументов ключевых слов.

родители
Свойство, возвращающее новое, ChainMap содержащее все карты в текущем экземпляре, кроме первой. Это полезно для пропуска первой карты при поиске. Варианты использования аналогичны вариантам для nonlocal ключевого слова, используемого во вложенных областях. Варианты использования также параллельны вариантам использования встроенной super() функции. Ссылка на d.parents эквивалентна: ChainMap(*d.maps[1:]).

Обратите внимание, порядок итераций a ChainMap() определяется путем сканирования сопоставлений от последнего к первому:

>>>
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
 (корректировки, базовыйуровень))
["музыка", "искусство", "опера"]
Это дает тот же порядок, что и серия dict.update() вызовов, начинающихся с последнего сопоставления:

>>>
комбинированный = базовый уровень.копировать()
комбинированный.обновление(корректировки)
список(комбинированный)
['музыка', 'искусство', 'опера']
Изменено в версии 3.9: добавлена поддержка операторов | и |=, указанных в PEP 584.

See also
The MultiContext class in the Enthought CodeTools package has options to support writing to any mapping in the chain.

Django’s Context class for templating is a read-only chain of mappings. It also features pushing and popping of contexts similar to the new_child() method and the parents property.

The Nested Contexts recipe has options to control whether writes and other mutations apply only to the first mapping or to any mapping in the chain.

A greatly simplified read-only version of Chainmap.

ChainMap Examples and Recipes
This section shows various approaches to working with chained maps.

Example of simulating Python’s internal lookup chain:

import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))
Пример предоставления заданным пользователем аргументам командной строки приоритета над переменными среды, которые, в свою очередь, имеют приоритет над значениями по умолчанию:

импорт ОС, argparse

умолчанию = {'color': 'red', 'user': 'guest'}

анализатор = argparse.ArgumentParser()
Синтаксический анализатор.add_argument('-u', '--user')
синтаксический анализатор.add_argument('-c', '--color')
пространство имен = синтаксический анализатор.parse_args()
command_line_args =  {k: v для k, v в vars(пространство имен).items() если v   

    
 цветной"])
печать(комбинированная["пользователь"])
Примеры шаблонов для использования ChainMap класса для имитации вложенных контекстов:

c = ChainMap()        # Создать корневой контекст
d = c.new_child()     # Создать вложенный дочерний контекст
e = c.new_child()     # Дочерний элемент c, независимый от d
e.maps[0]             # Словарь текущего контекста - как locals() в Python
e.maps[-1]            # Корневой контекст - как globals в Python() 
e.parents             # Заключающая контекстная цепочка - как нелокальные файлы Python

d['x'] = 1            # Установить значение в текущем контексте
d['x']                # Получить первый ключ в цепочке контекстов
del d['x']            # Удалить из 
списка текущего контекста (d)               # Все вложенные значения
k в d                # Проверить все вложенные значения
len(d)                # Количество вложенных значений
d.элементы ( )             # Все вложенные элементы
dict(d)               # Сгладить в обычный словарь
ChainMap Класс выполняет обновления (записи и удаления) только для первого сопоставления в цепочке, в то время как поисковые системы будут выполнять поиск по всей цепочке. Однако, если требуются глубокие записи и удаления, легко создать подкласс, который обновляет ключи, находящиеся глубже в цепочке:

class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

>>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
>>> d['lion'] = 'orange'         # update an existing key two levels down
>>> d['snake'] = 'red'           # new keys get added to the topmost dict
>>> del d['elephant']            # remove an existing key one level down
>>> d                            # display result
DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})
Counter objects
A counter tool is provided to support convenient and rapid tallies. For example:

>>>
# Tally occurrences of words in a list
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]
class collections.Counter([iterable-or-mapping])
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

Elements are counted from an iterable or initialized from another mapping (or counter):

>>>
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:

>>>
c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero
0
Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:

>>>
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry
New in version 3.1.

Changed in version 3.7: As a dict subclass, Counter inherited the capability to remember insertion order. Math operations on Counter objects also preserve order. Results are ordered according to when an element is first encountered in the left operand and then by the order encountered in the right operand.

Объекты-счетчики поддерживают дополнительные методы, помимо тех, которые доступны для всех словарей:

элементы()
Возвращает итератор по элементам, повторяющийся каждый столько раз, сколько его количество. Элементы возвращаются в порядке, в котором они были обнаружены первыми. Если количество элементов меньше единицы, elements() игнорирует его.

>>>
c = Счетчик(a=4, b=2, c=0, d=-2)
отсортировано(c.элементы())
['a', 'a', 'a', 'a', 'b' , 'b']
most_comm([n])
Возвращает список из n наиболее распространенных элементов и их количество от наиболее распространенных до наименьшего. Если значение n опущено или None, most_common() возвращает все элементы в счетчике. Элементы с равным количеством элементов упорядочиваются в порядке, в котором они были обнаружены первыми.:

>>>
Счетчик('abracadabra').most_comm(3)
[('a', 5), ('b', 2), ('r', 2)]
subtract([iterable-or-mapping])
Элементы вычитаются из итерируемого объекта или из другого сопоставления (или счетчика). Like dict.update() но вычитает значения вместо их замены. Как входные, так и выходные данные могут быть нулевыми или отрицательными.

>>>
c = Счетчик(a=4, b=2, c=0, d=-2)
d = Счетчик(a=1, b=2, c= 3, d=4)
c.вычесть(d)
c
({'a': 3, 'b': 0, 'c': -3, 'd': -6})
Новое в версии 3.2.

всего()
Compute the sum of the counts.

>>>
c = Counter(a=10, b=5, c=0)
c.total()
15
New in version 3.10.

The usual dictionary methods are available for Counter objects except for two which work differently for counters.

fromkeys(iterable)
This class method is not implemented for Counter objects.

update([iterable-or-mapping])
Elements are counted from an iterable or added-in from another mapping (or counter). Like dict.update() but adds counts instead of replacing them. Also, the iterable is expected to be a sequence of elements, not a sequence of (key, value) pairs.

Counters support rich comparison operators for equality, subset, and superset relationships: ==, !=, <, <=, >, >=. All of those tests treat missing elements as having zero counts so that Counter(a=1) == Counter(a=1, b=0) returns true.

New in version 3.10: Rich comparison operations were added.

Changed in version 3.10: In equality tests, missing elements are treated as having zero counts. Formerly, Counter(a=3) and Counter(a=3, b=0) were considered distinct.

Common patterns for working with Counter objects:

c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
Several mathematical operations are provided for combining Counter objects to produce multisets (counters that have counts greater than zero). Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements. Intersection and union return the minimum and maximum of corresponding counts. Equality and inclusion compare corresponding counts. Each operation can accept inputs with signed counts, but the output will exclude results with counts of zero or less.

>>>
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
c == d                      # equality:  c[x] == d[x]
False
c <= d                      # inclusion:  c[x] <= d[x]
False
Unary addition and subtraction are shortcuts for adding an empty counter or subtracting from an empty counter.

>>>
c = Counter(a=2, b=-4)
+c
Counter({'a': 2})
-c
Counter({'b': 4})
New in version 3.3: Added support for unary plus, unary minus, and in-place multiset operations.

Note Counters were primarily designed to work with positive integers to represent running counts; however, care was taken to not unnecessarily preclude use cases needing other types or negative values. To help with those use cases, this section documents the minimum range and type restrictions.
The Counter class itself is a dictionary subclass with no restrictions on its keys and values. The values are intended to be numbers representing counts, but you could store anything in the value field.

The most_common() method requires only that the values be orderable.

For in-place operations such as c[key] += 1, the value type need only support addition and subtraction. So fractions, floats, and decimals would work and negative values are supported. The same is also true for update() and subtract() which allow negative and zero values for both inputs and outputs.

The multiset methods are designed only for use cases with positive values. The inputs may be negative or zero, but only outputs with positive values are created. There are no type restrictions, but the value type needs to support addition, subtraction, and comparison.

The elements() method requires integer counts. It ignores zero and negative counts.

See also
Bag class in Smalltalk.

Wikipedia entry for Multisets.

C++ multisets tutorial with examples.

For mathematical operations on multisets and their use cases, see Knuth, Donald. The Art of Computer Programming Volume II, Section 4.6.3, Exercise 19.

To enumerate all distinct multisets of a given size over a given set of elements, see itertools.combinations_with_replacement():

map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC
deque objects
class collections.deque([iterable[, maxlen]])
Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Deque objects support the following methods:

append(x)
Add x to the right side of the deque.

appendleft(x)
Add x to the left side of the deque.

очистить()
Удалите все элементы из deque, оставив ему длину 0.

копировать()
Создайте поверхностную копию deque.

Новое в версии 3.5.

количество(x)
Подсчитайте количество элементов deque, равное x.

Новое в версии 3.2.

расширяемый(итерируемый)
Расширьте правую часть deque, добавив элементы из аргумента iterable .

extendleft(итерируемый)
Расширьте левую часть deque, добавив элементы из iterable. Обратите внимание, что последовательность добавлений слева приводит к изменению порядка элементов в аргументе iterable.

[x(index, start[, stop]])
Возвращает позицию x в deque (в начале индекса или после него и перед остановкой индекса). Возвращает первое совпадение или повышает значение ValueError если не найдено.

Новое в версии 3.5.

i(вставить, x)
Вставьте x в deque в позиции i.

Если вставка приведет к увеличению ограниченного значения deque за пределы maxlen, возникает IndexError запрос.

New in version 3.5.

pop()
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value)
Remove the first occurrence of value. If not found, raises a ValueError.

reverse()
Reverse the elements of the deque in-place and then return None.

New in version 3.2.

rotate(n=1)
Rotate the deque n steps to the right. If n is negative, rotate to the left.

When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

Deque objects also provide one read-only attribute:

maxlen
Maximum size of a deque or None if unbounded.

New in version 3.1.

In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d), membership testing with the in operator, and subscript references such as d[0] to access the first element. Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.

Starting in version 3.5, deques support __add__(), __mul__(), and __imul__().

Example:

>>>
from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())
G
H
I

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

d.pop()                          # return and remove the rightmost item
'j'
d.popleft()                      # return and remove the leftmost item
'f'
list(d)                          # list the contents of the deque
['g', 'h', 'i']
d[0]                             # peek at leftmost item
'g'
d[-1]                            # peek at rightmost item
'i'

list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
'h' in d                         # search the deque
True
d.extend('jkl')                  # add multiple elements at once
d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.rotate(1)                      # right rotation
d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)                     # left rotation
d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order
d
deque(['c', 'b', 'a'])
deque Recipes
This section shows various approaches to working with deques.

Bounded length deques provide functionality similar to the tail filter in Unix:

def tail(filename, n=10):
    'Return the last n lines of a file'
    with open(filename) as f:
        return deque(f, n)
Another approach to using deques is to maintain a sequence of recently added elements by appending to the right and popping to the left:

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # https://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n
A round-robin scheduler can be implemented with input iterators stored in a deque. Values are yielded from the active iterator in position zero. If that iterator is exhausted, it can be removed with popleft(); otherwise, it can be cycled back to the end with the rotate() method:

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            # Remove an exhausted iterator.
            iterators.popleft()
The rotate() method provides a way to implement deque slicing and deletion. For example, a pure Python implementation of del d[n] relies on the rotate() method to position elements to be popped:

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)
Для реализации deque нарезки используйте аналогичный подход, применяемый rotate() для переноса целевого элемента в левую часть списка. Удалите старые записи с помощью popleft(), добавьте новые записи с помощью extend(), а затем выполните обратное вращение. С небольшими вариациями этого подхода легко реализовать манипуляции со стеком в стиле Forth, такие как dup, drop, swap, over, pick rot, roll, ,,, и ,,,.

defaultdict объекты
default_factory=None (defaultdictcollections.class, /[, ...])
Возвращает новый объект, подобный словарю. defaultdict является подклассом встроенного dict класса. Он переопределяет один метод и добавляет одну доступную для записи переменную экземпляра. Остальные функциональные возможности те же, что и для dict класса, и здесь они не задокументированы.

Первый аргумент предоставляет начальное значение для default_factory атрибута; по умолчанию оно равно None. Все остальные аргументы обрабатываются так же, как если бы они были переданы в dict конструктор, включая аргументы ключевого слова.

defaultdict объекты поддерживают следующий метод в дополнение к стандартным dict операциям:

__отсутствует__(ключ)
Если default_factory атрибут равен None, это вызывает KeyError исключение с ключом в качестве аргумента.

Если default_factory нетNone, вызывается без аргументов, чтобы предоставить значение по умолчанию для данного ключа, это значение вставляется в словарь для ключа и возвращается.

Если вызов default_factory вызывает исключение, это исключение распространяется без изменений.

Этот метод вызывается __getitem__() методом dict класса, когда запрошенный ключ не найден; все, что он возвращает или создает, затем возвращается или создается с помощью __getitem__().

Note that __missing__() is not called for any operations besides __getitem__(). This means that get() will, like normal dictionaries, return None as a default rather than using default_factory.

defaultdict objects support the following instance variable:

default_factory
This attribute is used by the __missing__() method; it is initialized from the first argument to the constructor, if present, or to None, if absent.

Changed in version 3.9: Added merge (|) and update (|=) operators, specified in PEP 584.

defaultdict Examples
Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists:

>>>
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. This technique is simpler and faster than an equivalent technique using dict.setdefault():

>>>
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):

>>>
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1

sorted(d.items())
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]
When a letter is first encountered, it is missing from the mapping, so the default_factory function calls int() to supply a default count of zero. The increment operation then builds up the count for each letter.

The function int() which always returns zero is just a special case of constant functions. A faster and more flexible way to create constant functions is to use a lambda function which can supply any constant value (not just zero):

>>>
def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
'%(name)s %(action)s to %(object)s' % d
'John ran to <missing>'
Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:

>>>
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]
namedtuple() Factory Function for Tuples with Named Fields
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Instances of the subclass also have a helpful docstring (with typename and field_names) and a helpful __repr__() method which lists the tuple contents in a name=value format.

The field_names are a sequence of strings such as ['x', 'y']. Alternatively, field_names can be a single string with each fieldname separated by whitespace and/or commas, for example 'x y' or 'x, y'.

Any valid Python identifier may be used for a fieldname except for names starting with an underscore. Valid identifiers consist of letters, digits, and underscores but do not start with a digit or underscore and cannot be a keyword such as class, for, return, global, pass, or raise.

If rename is true, invalid fieldnames are automatically replaced with positional names. For example, ['abc', 'def', 'ghi', 'abc'] is converted to ['abc', '_1', 'ghi', '_3'], eliminating the keyword def and the duplicate fieldname abc.

defaults can be None or an iterable of default values. Since fields with a default value must come after any fields without a default, the defaults are applied to the rightmost parameters. For example, if the fieldnames are ['x', 'y', 'z'] and the defaults are (1, 2), then x will be a required argument, y will default to 1, and z will default to 2.

If module is defined, the __module__ attribute of the named tuple is set to that value.

Named tuple instances do not have per-instance dictionaries, so they are lightweight and require no more memory than regular tuples.

To support pickling, the named tuple class should be assigned to a variable that matches typename.

Changed in version 3.1: Added support for rename.

Changed in version 3.6: The verbose and rename parameters became keyword-only arguments.

Changed in version 3.6: Added the module parameter.

Changed in version 3.7: Removed the verbose parameter and the _source attribute.

Changed in version 3.7: Added the defaults parameter and the _field_defaults attribute.

>>>
# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
x, y = p                # unpack like a regular tuple
x, y
(11, 22)
p.x + p.y               # fields also accessible by name
33
p                       # readable __repr__ with a name=value style
Point(x=11, y=22)
Named tuples are especially useful for assigning field names to result tuples returned by the csv or sqlite3 modules:

EmployeeRecord = namedtuple('EmployeeRecord', 'имя, возраст, должность, отдел, уровень заработной платы')

импортируйте csv
для emp в map(EmployeeRecord._make, csv.reader(открыть("employees.csv", "rb"))):
    print(emp.название, emp.заголовок)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('ВЫБЕРИТЕ имя, возраст , должность, отдел, рейтинг заработной платы ИЗ данных сотрудников)
для emp на карте(EmployeeRecord._make, курсор.fetchall()):
    print(emp.name, emp.title)
В дополнение к методам, унаследованным от кортежей, именованные кортежи поддерживают три дополнительных метода и два атрибута. Чтобы предотвратить конфликты с именами полей, имена методов и атрибутов начинаются с подчеркивания.

метод класса somenamedtuple._make(итерируемый)
Метод класса, который создает новый экземпляр из существующей последовательности или повторяемый.

>>>
t = [11, 22]
Point._make(t)
Point(x=11, y=22)
somenamedtuple._asdict()
Возвращает новое значение, dict которое сопоставляет имена полей с их соответствующими значениями:

>>>
p = Point(x=11, y=22)
p._asdict()
{'x': 11, 'y': 22}
Изменено в версии 3.1: возвращает an OrderedDict вместо обычного dict.

Изменено в версии 3.8: возвращает обычное значение dict вместо OrderedDict. Начиная с Python 3.7, гарантируется упорядоченность обычных dicts. Если требуются дополнительные функции OrderedDict, предлагаемое исправление заключается в приведении результата к желаемому типу: OrderedDict(nt._asdict()).

somenamedtuple._replace(**kwargs)
Return a new instance of the named tuple replacing specified fields with new values:

>>>
p = Point(x=11, y=22)
p._replace(x=33)
Point(x=33, y=22)

for partnum, record in inventory.items():
    inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())
somenamedtuple._fields
Tuple of strings listing the field names. Useful for introspection and for creating new named tuple types from existing named tuples.

>>>
p._fields            # view the field names
('x', 'y')

Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
Pixel(11, 22, 128, 255, 0)
Pixel(x=11, y=22, red=128, green=255, blue=0)
somenamedtuple._field_defaults
Dictionary mapping field names to default values.

>>>
Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
Account._field_defaults
{'balance': 0}
Account('premium')
Account(type='premium', balance=0)
To retrieve a field whose name is stored in a string, use the getattr() function:

>>>
getattr(p, 'x')
11
To convert a dictionary to a named tuple, use the double-star-operator (as described in Unpacking Argument Lists):

>>>
d = {'x': 11, 'y': 22}
Point(**d)
Point(x=11, y=22)
Since a named tuple is a regular Python class, it is easy to add or change functionality with a subclass. Here is how to add a calculated field and a fixed-width print format:

>>>
class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
    print(p)
Point: x= 3.000  y= 4.000  hypot= 5.000
Point: x=14.000  y= 0.714  hypot=14.018
The subclass shown above sets __slots__ to an empty tuple. This helps keep memory requirements low by preventing the creation of instance dictionaries.

Subclassing is not useful for adding new, stored fields. Instead, simply create a new named tuple type from the _fields attribute:

>>>
Point3D = namedtuple('Point3D', Point._fields + ('z',))
Docstrings can be customized by making direct assignments to the __doc__ fields:

>>>
Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'
Changed in version 3.5: Property docstrings became writeable.

See also
See typing.NamedTuple for a way to add type hints for named tuples. It also provides an elegant notation using the class keyword:

class Component(NamedTuple):
    part_number: int
    weight: float
    description: Optional[str] = None
See types.SimpleNamespace() for a mutable namespace based on an underlying dictionary instead of a tuple.

The dataclasses module provides a decorator and functions for automatically adding generated special methods to user-defined classes.

OrderedDict objects
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. They have become less important now that the built-in dict class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).

Some differences from dict still remain:

The regular dict was designed to be very good at mapping operations. Tracking insertion order was secondary.

The OrderedDict was designed to be good at reordering operations. Space efficiency, iteration speed, and the performance of update operations were secondary.

The OrderedDict algorithm can handle frequent reordering operations better than dict. As shown in the recipes below, this makes it suitable for implementing various kinds of LRU caches.

The equality operation for OrderedDict checks for matching order.

A regular dict can emulate the order sensitive equality test with p == q and all(k1 == k2 for k1, k2 in zip(p, q)).

The popitem() method of OrderedDict has a different signature. It accepts an optional argument to specify which item is popped.

A regular dict can emulate OrderedDict’s od.popitem(last=True) with d.popitem() which is guaranteed to pop the rightmost (last) item.

A regular dict can emulate OrderedDict’s od.popitem(last=False) with (k := next(iter(d)), d.pop(k)) which will return and remove the leftmost (first) item if it exists.

OrderedDict has a move_to_end() method to efficiently reposition an element to an endpoint.

A regular dict can emulate OrderedDict’s od.move_to_end(k, last=True) with d[k] = d.pop(k) which will move the key and its associated value to the rightmost (last) position.

A regular dict does not have an efficient equivalent for OrderedDict’s od.move_to_end(k, last=False) which moves the key and its associated value to the leftmost (first) position.

Until Python 3.8, dict lacked a __reversed__() method.

class collections.OrderedDict([items])
Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.

New in version 3.1.

popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

move_to_end(key, last=True)
Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

>>>
d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d)
'acdeb'
d.move_to_end('b', last=False)
''.join(d)
'bacde'
New in version 3.2.

In addition to the usual mapping methods, ordered dictionaries also support reverse iteration using reversed().

Equality tests between OrderedDict objects are order-sensitive and are implemented as list(od1.items())==list(od2.items()). Equality tests between OrderedDict objects and other Mapping objects are order-insensitive like regular dictionaries. This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.

Changed in version 3.5: The items, keys, and values views of OrderedDict now support reverse iteration using reversed().

Changed in version 3.6: With the acceptance of PEP 468, order is retained for keyword arguments passed to the OrderedDict constructor and its update() method.

Changed in version 3.9: Added merge (|) and update (|=) operators, specified in PEP 584.

OrderedDict Examples and Recipes
It is straightforward to create an ordered dictionary variant that remembers the order the keys were last inserted. If a new entry overwrites an existing entry, the original insertion position is changed and moved to the end:

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
An OrderedDict would also be useful for implementing variants of functools.lru_cache():

from collections import OrderedDict
from time import time

class TimeBoundedLRU:
    "LRU Cache that invalidates and refreshes old entries."

    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()      # { args : (timestamp, result)}
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if time() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = time(), result
        if len(self.cache) > self.maxsize:
            self.cache.popitem(0)
        return result
class MultiHitLRUCache:
    """ LRU cache that defers caching a result until
        it has been requested multiple times.

        To avoid flushing the LRU cache with one-time requests,
        we don't cache until a request has been made more than once.

    """

    def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
        self.requests = OrderedDict()   # { uncached_key : request_count }
        self.cache = OrderedDict()      # { cached_key : function_result }
        self.func = func
        self.maxrequests = maxrequests  # max number of uncached requests
        self.maxsize = maxsize          # max number of stored return values
        self.cache_after = cache_after

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            return self.cache[args]
        result = self.func(*args)
        self.requests[args] = self.requests.get(args, 0) + 1
        if self.requests[args] <= self.cache_after:
            self.requests.move_to_end(args)
            if len(self.requests) > self.maxrequests:
                self.requests.popitem(0)
        else:
            self.requests.pop(args, None)
            self.cache[args] = result
            if len(self.cache) > self.maxsize:
                self.cache.popitem(0)
        return result
UserDict объекты
Класс, UserDict действует как оболочка вокруг объектов словаря. Необходимость в этом классе была частично вытеснена возможностью создания подкласса непосредственно из dict; однако с этим классом может быть проще работать, поскольку базовый словарь доступен как атрибут.

коллекции классов .UserDict([initialdata])
Класс, имитирующий словарь. Содержимое экземпляра хранится в обычном словаре, доступ к которому осуществляется через data атрибут UserDict экземпляров. Если initialdata предоставляется, data инициализируется его содержимым; обратите внимание, что ссылка на initialdata сохраняться не будет, что позволяет использовать его для других целей.

В дополнение к поддержке методов и операций сопоставлений, UserDict экземпляры предоставляют следующий атрибут:

данные
Реальный словарь, используемый для хранения содержимого UserDict класса.

UserList объекты
Этот класс действует как оболочка вокруг объектов списка. Это полезный базовый класс для ваших собственных классов, похожих на списки, которые могут наследоваться от них и переопределять существующие методы или добавлять новые. Таким образом, можно добавлять новое поведение к спискам.

Необходимость в этом классе была частично вытеснена возможностью создания подкласса непосредственно из list; однако с этим классом может быть проще работать, поскольку базовый список доступен как атрибут.

коллекции классов .Список пользователей([список])
Класс, имитирующий список. Содержимое экземпляра хранится в обычном списке, доступ к которому осуществляется через data атрибут UserList экземпляров. Содержимое экземпляра изначально устанавливается в копию list, по умолчанию в пустой список []. список может быть любым итеративным, например реальным списком Python или UserList объектом.

В дополнение к поддержке методов и операций с изменяемыми последовательностями, UserList экземпляры предоставляют следующий атрибут:

данные
Реальный list объект, используемый для хранения содержимого UserList класса.

Требования к подклассам: Ожидается, что подклассы UserList будут предлагать конструктор, который может вызываться либо без аргументов, либо с одним аргументом. Операции со списком, которые возвращают новую последовательность, пытаются создать экземпляр фактического класса реализации. Для этого предполагается, что конструктор может быть вызван с одним параметром, который является объектом sequence, используемым в качестве источника данных.

Если производный класс не желает соответствовать этому требованию, все специальные методы, поддерживаемые этим классом, необходимо будет переопределить; пожалуйста, обратитесь к источникам за информацией о методах, которые необходимо предоставить в этом случае.

UserString объекты
Класс, UserString действует как оболочка вокруг строковых объектов. Необходимость в этом классе была частично вытеснена возможностью создания подкласса непосредственно из str; однако с этим классом может быть проще работать, поскольку базовая строка доступна как атрибут.

класс collections.Пользовательская строка(seq)
Класс, имитирующий объект string. Содержимое экземпляра хранится в обычном объекте string, доступ к которому осуществляется через data атрибут UserString экземпляров. Содержимое экземпляра изначально устанавливается в виде копии seq. Аргументом seq может быть любой объект, который может быть преобразован в строку с помощью встроенной str() функции.

В дополнение к поддержке методов и операций со строками, UserString экземпляры предоставляют следующий атрибут:

данные
Реальный str объект, используемый для хранения содержимого UserString класса.

Изменено в версии 3.5: новые методы __getnewargs__, __rmod__, casefold format_map, isprintable maketrans, и,,,.'''
text = ''.join(text.split('\n')).strip()
text = re.sub('[^A-Za-z]+', ' ', text.lower())
lst = text.split()

print(f'Number of unique words: {len(Counter(lst))}')

print(f'Top-10: {Counter(lst).most_common(10)}')


