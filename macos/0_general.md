# macOS workshop

## Intro

macOS is build on top of XNU kernel, with user space parts derived from FreeBSD.
[XNU source code](https://github.com/apple-oss-distributions/xnu)

A lot of the built-in tools are just forks of the usual suspects...
With some missing options and flags.
eg `tcpdump`, `netcat`, `traceroute`, `ping`, `lsof`
[Included software](https://github.com/apple-oss-distributions/distribution-macOS)

Some of the output formatting might be different too.

For example: `nc -nlv 1000` is actually missing the verbose output
that is present in the Linux version.

## Network configuration

`ifconfig` is still used instead of `ip` command.

```sh
sudo ifconfig utun10 add 100.107.248.167/10 100.107.248.167
sudo ifconfig utun10 mtu 1420
sudo ifconfig utun10 up
```

## Package manager

No built in package manager, but defacto standard is
the third party open-source [Homebrew](https://brew.sh/)

```sh
brew install iperf3 # install iperf
brew install --cask wireshark # install wireshark
```

## Build tools

`clang` and `lldb` is used instead of `gcc` and `gdb`.
It is possible t install the GNU tools through brew,
but it will most likely break stuff.

`gcc` is just a wrapper for `clang`

```sh
gcc --version

Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin24.4.0
Thread model: posix
InstalledDir: /Applications/Xcode-16.2.0.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```
