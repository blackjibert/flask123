from flask import globals

## flask中的Local
class Local:
    __slots__ = ("_storage",)

    def __init__(self) -> None:
        object.__setattr__(self, "_storage", ContextVar("local_storage"))

    @property
    def __storage__(self) -> t.Dict[str, t.Any]:
        warnings.warn(
            "'__storage__' is deprecated and will be removed in Werkzeug 2.1.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._storage.get({})  # type: ignore

    @property
    def __ident_func__(self) -> t.Callable[[], int]:
        warnings.warn(
            "'__ident_func__' is deprecated and will be removed in"
            " Werkzeug 2.1. It should not be used in Python 3.7+.",
            DeprecationWarning,
            stacklevel=2,
        )
        return _get_ident  # type: ignore

    @__ident_func__.setter
    def __ident_func__(self, func: t.Callable[[], int]) -> None:
        warnings.warn(
            "'__ident_func__' is deprecated and will be removed in"
            " Werkzeug 2.1. Setting it no longer has any effect.",
            DeprecationWarning,
            stacklevel=2,
        )

    def __iter__(self) -> t.Iterator[t.Tuple[int, t.Any]]:
        return iter(self._storage.get({}).items())

    def __call__(self, proxy: str) -> "LocalProxy":
        """Create a proxy for a name."""
        return LocalProxy(self, proxy)

    def __release_local__(self) -> None:
        __release_local__(self._storage)

    def __getattr__(self, name: str) -> t.Any:
        values = self._storage.get({})
        try:
            return values[name]
        except KeyError:
            raise AttributeError(name) from None

    def __setattr__(self, name: str, value: t.Any) -> None:
        values = self._storage.get({}).copy()
        values[name] = value
        self._storage.set(values)

    def __delattr__(self, name: str) -> None:
        values = self._storage.get({}).copy()
        try:
            del values[name]
            self._storage.set(values)
        except KeyError:
            raise AttributeError(name) from None
