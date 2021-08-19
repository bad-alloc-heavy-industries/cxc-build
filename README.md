# GCC Cross Compiler build script

`cxc-build` is a python script that builds a large collection of GCC cross compilers for various platforms.

## What is built

`GMP`, `MPFR`, and `MPC` are built only once as they are shared between all of the toolchains built by this script. `binutils`, `gdb`, `gcc`, and `newlib` are then built for each of the selected targets.

## Currently Supported Targets

| Target                    | Binutils | GDB | GCC  | libc    |
|---------------------------|----------|-----|------|---------|
| `aarch64-none-elf`        | ✔        | ✔   | ✔    | newlib  |
| `aarch64-unknown-elf`     | ✔        | ✔   | ✔    | newlib  |
| `aarch64-unknown-linux`   | ✘        | ✘   | ✘    | glibc   |
| `arm-none-eabi`           | ✔        | ✔   | ✔    | newlib  |
| `arm-unknown-linux`       | ✘        | ✘   | ✘    | glibc   |
| `avr`                     | ✔        | ✔   | ✔    | avrlibc |
| `frv-none-elf`            | ✔        | ✔   | ✔    | newlib  |
| `frv-unknown-elf`         | ✔        | ✔   | ✔    | newlib  |
| `frv-unknown-linux`       | ✘        | ✘   | ✘    | glibc   |
| `ia64-none-elf`           | ✔        | ✘   | ✔    | newlib  |
| `ia64-unknown-elf`        | ✔        | ✘   | ✔    | newlib  |
| `ia64-unknown-linux`      | ✘        | ✘   | ✘    | glibc   |
| `microblaze-none-elf`     | ✔        | ✔   | ✔    | newlib  |
| `microblaze-unknown-elf`  | ✔        | ✔   | ✔    | newlib  |
| `microblaze-unknown-linux`| ✘        | ✘   | ✘    | glibc   |
| `mips-none-elf`           | ✔        | ✔   | ✔    | newlib  |
| `mips-unknown-elf`        | ✔        | ✔   | ✔    | newlib  |
| `mips-unknown-linux`      | ✘        | ✘   | ✘    | glibc   |
| `mips64-none-elf`         | ✔        | ✔   | ✔    | newlib  |
| `mips64-unknown-elf`      | ✔        | ✔   | ✔    | newlib  |
| `mips64-unknown-linux`    | ✘        | ✘   | ✘    | glibc   |
| `or1k-none-elf`           | ✔        | ✔   | ✔    | newlib  |
| `or1k-unknown-elf`        | ✔        | ✔   | ✔    | newlib  |
| `or1k-unknown-linux`      | ✘        | ✘   | ✘    | glibc   |
| `m68k-none-elf`           | ✔        | ✔   | ✔    | newlib  |
| `m68k-unknown-elf`        | ✔        | ✔   | ✔    | newlib  |
| `m68k-unknown-linux`      | ✘        | ✘   | ✘    | glibc   |
| `lm32-none-elf`           | ✔        | ✔   | ✔    | newlib  |
| `ppcle-none-elf`          | ✔        | ✔   | ✔    | newlib  |
| `ppcle-none-eabi`         | ✔        | ✔   | ✔    | newlib  |
| `ppcle-unknown-elf`       | ✔        | ✔   | ✔    | newlib  |
| `ppcle-unknown-linux`     | ✘        | ✘   | ✘    | glibc   |
| `ppc-none-elf`            | ✔        | ✔   | ✔    | newlib  |
| `ppc-none-eabi`           | ✔        | ✔   | ✔    | newlib  |
| `ppc-unknown-elf`         | ✔        | ✔   | ✔    | newlib  |
| `ppc-unknown-linux`       | ✘        | ✘   | ✘    | glibc   |
| `ppc64le-none-elf`        | ✔        | ✔   | ✘    | none    |
| `ppc64le-none-eabi`       | ✘        | ✘   | ✘    | none    |
| `ppc64le-unknown-elf`     | ✔        | ✔   | ✘    | none    |
| `ppc64le-unknown-linux`   | ✘        | ✘   | ✘    | none    |
| `ppc64-none-elf`          | ✔        | ✔   | ✘    | none    |
| `ppc64-none-eabi`         | ✘        | ✘   | ✘    | none    |
| `ppc64-unknown-elf`       | ✔        | ✔   | ✘    | none    |
| `ppc64-unknown-linux`     | ✘        | ✘   | ✘    | none    |
| `riscv32-none-elf`        | ✔        | ✔   | ✔    | newlib  |
| `riscv32-unknown-elf`     | ✔        | ✔   | ✔    | newlib  |
| `riscv32-unknown-linux`   | ✘        | ✘   | ✘    | glibc   |
| `riscv64-none-elf`        | ✔        | ✔   | ✔    | newlib  |
| `riscv64-unknown-elf`     | ✔        | ✔   | ✔    | newlib  |
| `riscv64-unknown-linux`   | ✘        | ✘   | ✘    | glibc   |
| `rx-none-elf`             | ✔        | ✔   | ✔    | newlib  |
| `rx-unknown-elf`          | ✔        | ✔   | ✔    | newlib  |
| `rx-unknown-linux`        | ✘        | ✘   | ✘    | glibc   |
| `s390-unknown-linux`      | ✘        | ✘   | ✘    | none    |
| `s390x-ibm-tpf`           | ✔        | ✘   | ✘    | none    |
| `s390x-unknown-linux`     | ✘        | ✘   | ✘    | none    |
| `sh4-none-elf`            | ✔        | ✔   | ✘    | none    |
| `sh4-unknown-elf`         | ✔        | ✔   | ✘    | none    |
| `sh4-unknown-linux`       | ✘        | ✘   | ✘    | none    |
| `sparc-none-elf`          | ✔        | ✔   | ✔    | newlib  |
| `sparc-unknown-elf`       | ✔        | ✔   | ✔    | newlib  |
| `sparc-unknown-linux`     | ✘        | ✘   | ✘    | glibc   |
| `sparc64-none-elf`        | ✔        | ✔   | ✘    | none    |
| `sparc64-unknown-elf`     | ✔        | ✔   | ✘    | none    |
| `sparc64-unknown-linux`   | ✘        | ✘   | ✘    | glibc   |
| `x86_64-none-elf`         | ✔        | ✔   | ✔    | newlib  |
| `x86_64-unknown-elf`      | ✔        | ✔   | ✔    | newlib  |
| `x86_64-unknown-linux`    | ✘        | ✘   | ✘    | glibc   |
| `hppa-none-elf`           | ✔        | ✔   | ✘    | none    |
| `hppa-unknown-elf`        | ✔        | ✔   | ✘    | none    |
| `hppa64-none-elf`         | ✔        | ✔   | ✘    | none    |
| `hppa64-unknown-elf`      | ✔        | ✔   | ✘    | none    |
| `hppa1.1-hp-hpux10`       | ✔        | ✘   | ✔    | none    |
| `hppa1.1-hp-hpux11`       | ✔        | ✘   | ✔    | none    |
| `hppa2.0-hp-hpux10`       | ✔        | ✘   | ✔    | none    |
| `hppa2.0-hp-hpux11`       | ✔        | ✘   | ✔    | none    |

## TODO

There are a few things that need to be fixed or added. They are as follows.

* Allow for selection of install and build paths at execution time without the need to edit the script
* Allow for selection of targets to build and/or not build
* Fix the `x-unknown-linux` targets so they build and then enable them

## License

This script is licensed under the BSD 3 Clause, the full text of which can be found in the [`LICENSE`](./LICENSE) file.
