+++
date = 2020-08-20T21:00:00Z
lastmod = 2020-08-20T21:00:00Z
title = "C Development"
subtitle = "C programming development guide and gotchas"
# feature = "image/page-default.webp"
# caption = "Feature image caption and image alt text."
+++

> This post is in progress

## make

The `make` command line utility can be used to help you organize the build
process of your project.

### make - Tip and Ticks

- Use the `-j` flag to have make compile with all the cores on your machine.
  This will speed up your builds when you have many files. If you're having
  trouble reading the errors, remove this flag to go back to using only one
  core.

## autotools

`autoconf` is a package which provides the tooling that a lot of long time C
projects use. Projects which use `autoconf` have files such as

- `bootstrap`
- `bootstrap.sh`
- `configure`
- `configure.sh`
- `configure.ac`
- `Makefile.am`

You'll hear these projects referred to as "autoconf" or "autotools" based
projects.

### autotools - Troubleshooting

If you get issues with projects that have `bootstrap`, `configure.sh`, or
`configure.ac`, you likely need to make sure the following packages are
installed on your system. Typaclly you'll find you're missing `autoconf-archive`
or `pkg-config`. These can be the source of many m4 macro not found errors.

- automake
- autoconf
- autoconf-archive
- pkg-config
