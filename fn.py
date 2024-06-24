import util
from typing import Tuple
from util import A, B, T, Bool, Int, Str, Dict, Optional, Fun, List

_id = util._id
_lam: Fun[[A], Fun[[T], A]] = lambda x: lambda *_: x
_traverse = util._traverse
_map = util._map
__map: Fun[[Fun], Fun[[List[A]], List[B]]] = lambda f: lambda l: _map(l, f)
_filter = util._filter
__filter: Fun[[Fun], Fun[[List[A]], List[B]]] = lambda f: lambda l: _filter(l, f)
_reduce = util._reduce
__reduce: Fun[[Fun], Fun[[List[A]], List[B]]] = lambda f, acc: lambda l: _reduce(l, f, acc)
_partition: Fun[[Fun], Fun[[List[A]], List[B]]] = lambda f: lambda l: _reduce(l, lambda acc, x: [acc[0] + ([x] if f(x) else [])] + [acc[1] + ([x] if not f(x) else [])], [[], []])
_maybe = util._maybe
_compose = util._compose
_csce = util._csce
_toTup = util._toTup

_either = lambda v, c, r, l: r(v) if c(v) else l(v)

_m = _map
__m = __map
_f = _filter
__f = __filter
_r = _reduce
_ma = _maybe
_c = _compose

_true: Fun[[], Bool] = _lam(True)
_false: Fun[[], Bool] = _lam(False)
_none: Fun[[], None] = _lam(None)

_not: Fun[[Bool], Bool] = lambda x: not x
_if: Fun[[[Bool]], Fun[[A], Fun[[B], A or B]]] = lambda c: lambda x: lambda y: x if c else y
_and: Fun[[Bool], Fun[[Bool], Bool]] = lambda a: lambda b: a and b
_or: Fun[[Bool], Fun[[Bool], Bool]] = lambda a: lambda b: a or b
_eq: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: x == y
_neq: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: not _eq(x)(y)
_lg: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: x > y
_lge: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: x >= y
_sm: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: x < y
_sme: Fun[[A], Fun[[B], Bool]] = lambda x: lambda y: x <= y

_int = lambda x: int(x)
_str = lambda x: str(x)

_len: Fun[[List[T]], Int] = lambda l: len(l)
_fst: Fun[[List[T]], T] = lambda l: l[0] if (type(l) == list or type(l) == tuple) and len(l) > 0 else None
_snd: Fun[[List[T]], T] = lambda l: l[1] if (type(l) == list or type(l) == tuple) and len(l) > 1 else None
_join: Fun[[Str], Fun[[List[Str]], Str]] = lambda s = "": lambda l: s.join(l)
_in: Fun[[List[T]], Fun[[T], Bool]] = lambda l: lambda x: x in l
_nin: Fun[[Fun[[List[T]], Bool]], T] = lambda l: lambda x: not _in(l)(x)
_include: Fun[[List[T]], Fun[[List[T]], List[T]]] = lambda l: lambda xs: _filter(l, _in(xs))
_exclude: Fun[[List[T]], Fun[[List[T]], List[T]]] = lambda l: lambda xs: _filter(l, _nin(xs))
_diff: Fun[[List[T]], Fun[[List[T]], List[T]]] = lambda l: lambda xs: _exclude(l)(xs) + _exclude(xs)(l)
_flatten: Fun[[List[T]], List[T]] = lambda l: _reduce(l, lambda acc, x: acc + (x if type(x) == list else [x]), [])
_sort = util._sort

_key: Fun[[Str], Fun[[Dict], T]] = lambda k: lambda d: d[k]
_todict: Fun[[List], Dict] = lambda l: _reduce(l, lambda x, acc: x | acc, {})
_omit: Fun[[List], Fun[[Dict], Dict]] = lambda l: lambda d: util._omit(d, l)
_keys: Fun[[Dict], List[str]] = lambda d: list(d.keys())
_vals: Fun[[Dict], List[str]] = lambda d: list(d.values())
_fkeys: Fun[[Dict], Str] = _c(_keys, _fst)
_fvals: Fun[[Dict], T] = _c(_vals, _fst)
_tup: Fun[[Dict], Tuple[A, B]] = lambda d: list(d.items())

_isnone: Fun[[T], Bool] = lambda x: x == None
_isstr: Fun[[T], Bool] = lambda x: type(x) == str
_isint: Fun[[T], Bool] = lambda x: type(x) == int
_islist: Fun[[T], Bool] = lambda x: type(x) == list

_split: Fun[[Str], Fun[[List[Str]], List[Str]]] = lambda s: lambda t: t.split(s)
_startswith: Fun[[Str], Fun[[Str], Bool]] = lambda a: lambda s: s.startswith(a)

_lower: Fun[[Str], Str] = lambda s: s.lower()

_find: Fun[[T, T], Fun[[Dict], Optional[T]]] = lambda k, fa = _id, fb = _id: lambda d: fa(util._tFind(d, k, fb))
_trace: Fun[[Str], Fun[[Dict], Optional[T]]] = lambda s: lambda d: util._trace(d, s)

# Note: not quite nice
def _setDict(k: Optional[Str]):
    def fa(f: Fun):
        def fb(d: Dict):
            def mutate(d_, k_, _):
                if (k):
                    d_[k_] = f(d_[k_])
                # else:
                    # d = f(d)

            _find(k, _id, mutate)(d)

            return d
        return fb
    return fa

# Maybes
_mfst = lambda xs = [], r = _id, l = _none: _maybe(_fst(xs), r, l)
_msnd = lambda xs = [], r = _id, l = _none: _maybe(_snd(xs), r, l)
_mkey = lambda k, r = _id, l = _lam("none"): lambda d: _maybe(d[k] if k in d else None, r, l)
_mfind = lambda k, r = _id, l = _none: lambda d: _maybe(_find(k)(d), r, l)
_mtrace = lambda s, r = _id, l = _none: lambda d: _maybe(_trace(s)(d), r, l)
_msplit = lambda s, r = _id, l = _none: lambda t: _maybe(_split(s)(t) if (_isstr(s) and _isstr(t)) else None, r, l)
_mjoin = lambda s, r = _id, l = _none: lambda a: _maybe(_join(s)(a) if (_islist(a) and _isstr(s)) else None, r, l)
_mint = lambda s, r = _id, l = _none: _maybe(_int(s) if _isstr(s) else None, r, l)
_mlower = lambda s, r = _id, l = _none: _maybe(_lower(s) if _isstr(s) else None, r, l)
