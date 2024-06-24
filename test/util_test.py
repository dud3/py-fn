import util
import fn.fn as fn

# Tree find
tree = {
	"a": {
		"aa": {},
		"ab": {},
				"ac": "a"
	},
	"b": {
			"ba": {},
			"bb": {}
	},
	"c": {
		"ca": {},
		"cb": {},
		"cc": []
	},
	"d": {
		"da": {
			"daa": {},
			"dab": "test"
		}
	},
	"e": {
		"ea": {
			"eaa": 0,
			"eab": [{"eaba": 0, "eabb": 1}]
		}
	},
	"f": {
		"fa": [{"faa": { "faaa": 1 }}, {"fab": { "faab": 2 }}]
	}
}

ifs0 = {
    "interfaces": {
		"interface": [
			{
				"name": "xe-0/2/2",
				"description": "Zayo 10GB link to Hosted Advantage 29-apr-2022 -jra (BACKUP PORT)",
				"unit": [{
					"name": 0,
					"family": {
						"ethernet-switching": {
							"interface-mode": "trunk",
							"vlan": {
								"members": [
									"RHZ_CLIENT1",
									"RHY_CLIENT2",
									"RHA_MGMT"
								]
							}
						}
					}
				}]
			},
			{
				"name": "xe-0/2/3",
				"description": "Zayo 10GB link to Hosted Advantage 29-apr-2022 -jra (BACKUP PORT)",
				"unit": [{
					"name": 0,
					"family": {
						"ethernet-switching": {
							"interface-mode": "trunk",
							"vlan": {
								"members": [
									"RHA_A"
									"RHA_B",
									"RHA_C",
								]
							}
						}
					}
				}]
			},
			{
				"name": "xe-0/2/3",
				"description": "Zayo 10GB link to Hosted...",
				"unit": [{
					"name": 0,
					"family": {
						"ethernet-switching": {
							"interface-mode": "access",
							"vlan": {
								"members": [
									"RHA_B",
                                    "RHA_A"
								]
							}
						}
					}
				}]
			},
            {
				"name": "xe-0/2/4",
				"description": "Zayo 10GB link to Hosted...",
				"unit": []
			},
            {
				"name": "xe-0/2/4",
				"description": "Zayo 10GB link to Hosted...",
				"unit": []
			},
            {
				"name": "ge-1/0/0",
				"description": "To ISCSI LACP Ernie-A e0d",
				"ether-options": {
					"ieee-802.3ad": {
						"bundle": "ae1"
					}
				}
			},
			{
				"name": "ge-1/0/1",
				"description": "To ISCSI LACP Ernie-B e0c",
				"ether-options": {
					"ieee-802.3ad": {
						"bundle": "ae2"
					}
				}
			},
			{
				"name": "ae1",
				"description": "WAN_INTERFACE of PA850",
				"mtu": 9192,
				"aggregated-ether-options": {
					"lacp": {
						"active": [
							None
						],
						"periodic": "fast"
					}
				},
				"unit": [
					{
						"name": 0,
						"family": {
							"ethernet-switching": {
								"interface-mode": "access",
								"vlan": {
									"members": [
										"R_VPNWAN_Glue"
									]
								}
							}
						}
					}
				]
			},
			{
				"name": "ae2",
				"description": "Trunk to ISCSI LACP Ernie-B e0c e0d",
				"mtu": 9192,
				"aggregated-ether-options": {
					"flow-control": [
						None
					],
					"lacp": {
						"active": [
							None
						],
						"periodic": "fast"
					}
				},
            	"unit": [
					{
						"name": 0,
						"family": {
							"ethernet-switching": {
								"interface-mode": "access",
								"vlan": {
									"members": [
										"ISCSI_RC"
									]
								}
							}
						}
					}
				]
			}
		]
	}
}


print("\n>> x")
print(util._tFind(tree, "x"))

print("\n>> a")
print(util._tFind(tree, "a"))

print("\n>> c")
print(util._tFind(tree, "c"))

print("\n>> cc")
print(util._tFind(tree, "cc"))

print("\n>> ab")
print(util._tFind(tree, "ab"))

print("\n>> ay")
print(util._tFind(tree, "ay"))

print("\n>> daa")
print(util._tFind(tree, "daa"))

print("\n>> dab")
print(util._tFind(tree, "dab"))

print("\n>> eab")
print(util._tFind(tree, "eab"))

print("\n>> eaba")
print(util._tFind(tree, "eaba"))

print("\n>> eabb")
print(util._tFind(tree, "eabb"))

print("\n>> faaa")
print(util._tFind(tree, "faaa"))

print("\n>> faab")
print(util._tFind(tree, "faab"))

print("\n>> port-mode")
print(util._tFind(ifs0, "port-mode"))

print("\n>> members")
print(util._tFind(ifs0, "members"))

print("\n>> traverse")
util._traverse([0,1,2], lambda x: print(x))

print("\n>> _unique")
print(util._unique([0,1,1,2]))
print(util._unique(['a','b','b','c','c']))
print(util._unique(['x','y','z','w','w']))

print("\n>> _find")
print(util._find([{"a":0, "b":1}, {"a":1, "b":2}], lambda x,_,__: x["a"] == 0))
print(util._find([{"a":0, "b":1}, {"a":1, "b":2}], lambda x,_,__: x["a"] == 2))
print(util._find([{"a":0, "b":1}, {"a":1, "b":2}], lambda x,_,__: x["b"] == 2))

print("\n>> _csce")
print(util._csce([], "Something"))
print(util._csce(None, "Something"))
print(util._csce(0, "Something"))
print(util._csce("Something", None))

print("\n>> _maybe")
print(util._maybe(None, lambda a: print(a)))
print(util._maybe("Some", util._id))
print(fn._maybe(fn._trace("b")({"a": 1}), util._id, lambda: util._p("Left")))

print("\n>> _compose")
print(util._compose(lambda x: x + 1, lambda x: x * x)(1))
print(
	util._compose(lambda x: x + 1, lambda x: x * x, lambda x: x / 2)(1)
)

print("\n>> _wrap")
print(util._wrap1(0)(lambda x: x + 1)(1))

print("\n>> _if")
_ifa = fn._if(1 == 1)("a")
_ifb = fn._if(1 == 2)("b")
print(_ifa("b"))
print(_ifb("c"))

print("\n>> _wrap")
print(fn._startswith("x")("xyzw"))
print(fn._startswith("y")("xyzw"))
print(fn._filter(["xyzw", "yzwx"], fn._startswith("x")))
print(fn._filter(["xyzw", "yzwx"], fn._startswith("y")))

print("\n>> _flatten")
print(fn._flatten([["a", "b", "c"]]))
print(fn._flatten([None]))
print(fn._flatten(["a", "b", "c"]))

print("\n>> _include")
print(fn._include(["a", "b", "c"])(["a", "b"]))
print(fn._include([{"a": 1}, {"b": 1}, {"c": 1}])([{"a": 1}, {"b": 1}]))

print("\n>> _exclude")
print(fn._exclude(["a", "b", "c"])(["a", "b"]))

print("\n>> _trace")
print(util._trace(None, ""))
print(util._trace([], ""))
print(util._trace({}, ""))
print(util._trace({"a": 1}, "a"))
print(util._trace({"a": {"b": 2}}, "a.b"))
print(util._trace({"a": {"b": {"c": 3}}}, "a.b.c"))
print(util._trace({"a": {"b": {"c": 3}}}, "a.b.c"))
print(util._trace({"a": {"b": {"c": {"d": [0,1,2]}}}}, "a.b.c"))

print(fn._trace("a.b.c.d")({"a": {"b": {"c": {"d": [0,1,2]}}}}))
print(fn._trace("a.b.c.d")({"a": {"b": {"c": [{"d": [0,1,2]}]}}}))
print(fn._trace("a.b.c.e")({"a": {"b": {"c": {"d": [0,1,2]}}}}))
print(fn._trace("a.y.c.d")({"a": {"b": {"c": {"d": [0,1,2]}}}}))

print("\n>> _lam")
print(fn._lam([])())
print(fn._lam("str")())
print(fn._lam(None)())

print("\n >> _mfst")
print(fn._mfst(None))
print(fn._mfst([]))
print(fn._mfst(['a', 'b', 'c']))
print(fn._mfst([0, 1, 2]))

print("\n>> _mtrace")
print(fn._mtrace("a.b")({"a": {"b": 2}}))
print(fn._mtrace("a.b", fn._id)({"a": {"b": 2}}))
print(fn._mtrace("a.b.c", fn._id, fn._lam(0))({"a": {"b": 2}}))
print(fn._mtrace("a.b.c", fn._id, fn._lam([]))({"a": {"b": 2}}))
print(fn._mtrace("d.da.dab", fn._id, fn._lam(""))(tree))

print("\n>> _mfind")
print(fn._mfind("a")(ifs0))
print(fn._mfind("data", lambda x: x == "ge-0/0/0")(ifs0))
print(fn._mfind("name", fn._id, fn._lam({}))(ifs0))
print(fn._mfind("data", fn._id, fn._lam(0))(ifs0))
print(fn._mfind("d.da.dab", fn._id, fn._lam(""))(tree))

# _either = lambda v, c, r, l: r(v) if c(v) else l(v)
print("\n>> _either")
print(fn._either([0], lambda x: len(x) > 0, lambda y: "Some", lambda z: None))

print("\n>> _keys")
print(fn._keys({"a": 0, "b": 1}))
print(fn._c(fn._keys, fn._fst)({"a": 0, "b": 1}))
print(fn._c(fn._vals, fn._fst)({"a": 0, "b": 1}))

print("\n>> _partition")
print(fn._partition(lambda x: x > 0)([-2, -1, 0, 1, 2]))

print("\n>> _setDict")
print(fn._setDict("b")(lambda x: x + 1)({"a": {"b": 2}}))
print(fn._setDict("b")(lambda x: x + 2)({"a": {"b": 2}}))
print(fn._setDict("b")(util._sort)({"a": {"b": [4, 3, 2, 1, 0]}}))

util._p(
	util._map(
		fn._mtrace("interfaces.interface", fn._id, fn._lam([]))(ifs0),
		fn._setDict("members")(fn._c(fn._sort, fn.__map(fn._lower)))
	)
)

print("\n>> _mjoin")
print(fn._join(",")(["a", "b"]))
print(fn._mjoin(",")(["a", "b", "c"]))

