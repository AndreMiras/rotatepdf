# How to release

This is documenting the release process.

We're using [calendar versioning](https://calver.org/) where `YYYY.MM.DD` should
be set accordingly.

```sh
VERSION=YYYY.MM.DD
```

## Start the release

```sh
git checkout -b release/$VERSION
```

Now update the [pyproject.toml](../pyproject.toml) `version` to match the new
release version.

```sh
sed --regexp-extended 's/^version = ".*"/version = "'"$VERSION"'"/' --in-place pyproject.toml
```

Then commit/push and create a pull request targeting the `master` branch.

```sh
git commit -a -m ":bookmark: v$VERSION"
git push origin release/$VERSION
```

Once the pull requests is approved/merged, tag the `master` branch with the
version. In the case of a sole owner, no pull request is required, but at least
verify the CI builds green.

```sh
git checkout master
git pull
git tag -a v$VERSION -m ":bookmark: v$VERSION"
git push --tags
```

## Publish to PyPI

This process is handled automatically by
[GitHub Actions](https://github.com/AndreMiras/rotatepdf/actions/workflows/pypi-release.yml).
If needed below are the instructions to perform it manually. Build it:

```sh
make release/build
```

Check archive content:

```sh
tar -tvf dist/rotatepdf-*.tar.gz
```

Upload:

```sh
make release/upload
```

## Release notes

You may want to add some GitHub release notes, by attaching a release to
[the newly pushed tag](https://github.com/AndreMiras/rotatepdf/tags).
