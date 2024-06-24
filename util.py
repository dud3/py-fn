from typing import TypeVar, Tuple, Callable, List, Dict, Optional
from inspect import signature
import json

T = TypeVar('T')
A = TypeVar('A')
B = TypeVar('B')

Str = str
Int = int
Float = float
Bool = bool
Some = T and not None
Fun = Callable
Mappable = Fun[[A], B]
Iterable = Callable[[A, Int, List], B]

def _id(a: A, i_: Int = 0, arr_: List[T] = []) -> A:
	return a

def _flip(tup: Tuple[A,B]) -> Tuple[B,A]:
	return (tup[1], tup[0])

def _none() -> None:
	return None

def _wrap1(a: T):
	return _id

def _compose(*fns: List[Callable]) -> Fun:
	return lambda x: _reduce(fns, lambda acc, f: f(acc), x)

def _maybe(a: Optional[A], fa: Mappable = _id, fn: Fun = _none):
	if a == None:
		return fn()

	return fa(a)

def _traverse(arr: List[A], fn: Iterable) -> None:
	if (len(arr) == 0): return None
	fn(arr[0])
	return _traverse(arr[1:], fn)

def _map(arr: List[A], fn: Iterable) -> List[B]:
	_arr = []
	args = len(signature(fn).parameters)

	for i, v in enumerate(arr):
		_arr.append(fn(v) if args == 1 else (fn(v,i) if args == 2 else fn(v,i,arr)))

	return _arr

def _filter(arr: List[A], fn: Iterable) -> List[A]:
	_arr = []
	args = len(signature(fn).parameters)

	for i, v in enumerate(arr):
		if (fn(v) if args == 1 else (fn(v,i) if args == 2 else fn(v,i,arr)) == True):
			_arr.append(v)

	return _arr

def _reduce(arr: List[A], fn: Fun, acc: A) -> Optional[T]:
	if (len(arr) == 0): return acc

	return _reduce(arr[1:], fn, fn(acc, arr[0]))

def _omit(d: Dict, keys: List[Str]) -> Dict:
	return {x: d[x] for x in d if x not in keys}

def _sort(arr: List[T]) -> List[T]:
	arr.sort() # note: skip fpr now
	return arr

def _list(x: Dict, i = 0, arr = []) -> List:
	return list(x.items())

def _keys(x: Dict, i = 0, arr = []) -> List[Str]:
	return list(x.keys())

def _vals(x: Dict, i = 0, arr = []) -> List[T]:
	return list(x.values())

def _tup(x: Dict, i = 0, arr = []):
	return list(x.items())[0]

def _toTup(x: List[T], i = 0, arr = []) -> Tuple[A, B]:
	return (x[0], x[1])

def _fst(tup: tuple[T], i: int = 0, arr: List[T] = []) -> T:
	return tup[0]

def _snd(tup: tuple[T], i: int = 0, arr: List[T] = []) -> T:
	return tup[1]

def _head(lst: List[T]) -> T:
	return lst[0]

def _tail(lst: List[T]) -> List[T]:
	return lst[1:]

def _csce(a: A, b: B) -> A or B:
	return (b if ((a == None) or (a == 0) or (a == []) or (a == "")) else a)

def _unique(e: T, i: int = 0, arr: List[T] = []) -> List[T]:
   return arr.index(e) == i

def _unique(lst: List[A]) -> List[B]:
	return _filter(lst, lambda x1,i1,a1: lst.index(x1) == i1)

def _splice(lst: List[A], i: Int) -> List[A]:
    del lst[i]
    return lst

def _strf(d: Dict) -> Str:
	return json.dumps(d, separators=(',', ':'))

def _find(lst: List[T], fn: Fun) -> Optional[T]:
	return _fst(_filter(lst, fn)) if len(_filter(lst, fn)) > 0 else None

def _tFind(d: dict or list, k: Str, fn: Fun = _id) -> Optional[T]:
	root = d
	if type(d) is list:
		for e in d:
			item = _tFind(e, k, fn)
			if (item): return item

	elif type(d) is dict:
		for key in d:
			if (key == k):
				if (fn != None): fn(d, k, root)

				return d[key]
			else:
				item = _tFind(d[key], k, fn)
				if (item): return item

def _trace(d: Dict, path: Str) -> Optional[T]:
	spath: List[T] = path.split('.')
	head = _head(spath)
	tail = _tail(spath)

	if type(d) is dict:
		if head in d:
			return d[head] if (len(tail) == 0) else _trace(d[head], ".".join(tail))
	elif type(d) is list:
		for e in d:
			return _trace(e, ".".join(tail))
	else:
		return None

def _pp(a: Dict) -> Str:
	return json.dumps(a, indent=2)

def _p(*args) -> None:
	_traverse(args, _compose(_pp, print))

def _pe(*args) -> None:
	_p(args)
	exit()
