# GCC Cross Compiler build script

`cxc-build` is a python script that builds a large collection of GCC cross compilers for various platforms.

## What is built

`GMP`, `MPFR`, and `MPC` are built only once as they are shared between all of the toolchains built by this script. `binutils`, `gdb`, `gcc`, and `newlib` are then built for each of the selected targets.

## Currently Supported Targets

| Target                    | Binutils | GDB | GCC  |
|---------------------------|----------|-----|------|
| `aarch64-none-elf`        | ✔        | ✔   | ✔    |
| `aarch64-unknown-elf`     | ✔        | ✔   | ✔    |
| `aarch64-unknown-linux`   | ✘        | ✘   | ✘    |
| `arm-none-eabi`           | ✔        | ✔   | ✔    |
| `arm-unknown-linux`       | ✘        | ✘   | ✘    |
| `frv-none-elf`            | ✔        | ✔   | ✔    |
| `frv-unknown-elf`         | ✔        | ✔   | ✔    |
| `frv-unknown-linux`       | ✘        | ✘   | ✘    |
| `ia64-none-elf`           | ✔        | ✘   | ✔    |
| `ia64-unknown-elf`        | ✔        | ✘   | ✔    |
| `ia64-unknown-linux`      | ✘        | ✘   | ✘    |
| `microblaze-none-elf`     | ✔        | ✔   | ✔    |
| `microblaze-unknown-elf`  | ✔        | ✔   | ✔    |
| `microblaze-unknown-linux`| ✘        | ✘   | ✘    |
| `mips-none-elf`           | ✔        | ✔   | ✔    |
| `mips-unknown-elf`        | ✔        | ✔   | ✔    |
| `mips-unknown-linux`      | ✘        | ✘   | ✘    |
| `mips64-none-elf`         | ✔        | ✔   | ✔    |
| `mips64-unknown-elf`      | ✔        | ✔   | ✔    |
| `mips64-unknown-linux`    | ✘        | ✘   | ✘    |
| `or1k-none-elf`           | ✔        | ✔   | ✔    |
| `or1k-unknown-elf`        | ✔        | ✔   | ✔    |
| `or1k-unknown-linux`      | ✘        | ✘   | ✘    |
| `m68k-none-elf`           | ✔        | ✔   | ✔    |
| `m68k-unknown-elf`        | ✔        | ✔   | ✔    |
| `m68k-unknown-linux`      | ✘        | ✘   | ✘    |
| `lm32-none-elf`           | ✔        | ✔   | ✔    |
| `ppcle-none-elf`          | ✔        | ✔   | ✔    |
| `ppcle-none-eabi`         | ✔        | ✔   | ✔    |
| `ppcle-unknown-elf`       | ✔        | ✔   | ✔    |
| `ppcle-unknown-linux`     | ✘        | ✘   | ✘    |
| `ppc-none-elf`            | ✔        | ✔   | ✔    |
| `ppc-none-eabi`           | ✔        | ✔   | ✔    |
| `ppc-unknown-elf`         | ✔        | ✔   | ✔    |
| `ppc-unknown-linux`       | ✘        | ✘   | ✘    |
| `ppc64le-none-elf`        | ✔        | ✔   | ✘    |
| `ppc64le-none-eabi`       | ✘        | ✘   | ✘    |
| `ppc64le-unknown-elf`     | ✔        | ✔   | ✘    |
| `ppc64le-unknown-linux`   | ✘        | ✘   | ✘    |
| `ppc64-none-elf`          | ✔        | ✔   | ✘    |
| `ppc64-none-eabi`         | ✘        | ✘   | ✘    |
| `ppc64-unknown-elf`       | ✔        | ✔   | ✘    |
| `ppc64-unknown-linux`     | ✘        | ✘   | ✘    |
| `riscv32-none-elf`        | ✔        | ✔   | ✔    |
| `riscv32-unknown-elf`     | ✔        | ✔   | ✔    |
| `riscv32-unknown-linux`   | ✘        | ✘   | ✘    |
| `riscv64-none-elf`        | ✔        | ✔   | ✔    |
| `riscv64-unknown-elf`     | ✔        | ✔   | ✔    |
| `riscv64-unknown-linux`   | ✘        | ✘   | ✘    |
| `rx-none-elf`             | ✔        | ✔   | ✔    |
| `rx-unknown-elf`          | ✔        | ✔   | ✔    |
| `rx-unknown-linux`        | ✘        | ✘   | ✘    |
| `s390-unknown-linux`      | ✘        | ✘   | ✘    |
| `s390x-ibm-tpf`           | ✔        | ✘   | ✘    |
| `s390x-unknown-linux`     | ✘        | ✘   | ✘    |
| `sh4-none-elf`            | ✔        | ✔   | ✘    |
| `sh4-unknown-elf`         | ✔        | ✔   | ✘    |
| `sh4-unknown-linux`       | ✘        | ✘   | ✘    |
| `sparc-none-elf`          | ✔        | ✔   | ✔    |
| `sparc-unknown-elf`       | ✔        | ✔   | ✔    |
| `sparc-unknown-linux`     | ✘        | ✘   | ✘    |
| `sparc64-none-elf`        | ✔        | ✔   | ✘    |
| `sparc64-unknown-elf`     | ✔        | ✔   | ✘    |
| `sparc64-unknown-linux`   | ✘        | ✘   | ✘    |
| `x86_64-none-elf`         | ✔        | ✔   | ✔    |
| `x86_64-unknown-elf`      | ✔        | ✔   | ✔    |
| `x86_64-unknown-linux`    | ✘        | ✘   | ✘    |


## TODO

There are a few things that need to be fixed or added. They are as follows.

 * Allow for selection of install and build paths at execution time without the need to edit the script
 * Allow for selection of targets to build and/or not build
 * Fix the `x-unknown-linux` targets so they build and then enable them
 * Add an `avr` target

## License

This script is licensed under the BSD 3 Clause, the full text of which can be found in the [`LICENSE`](./LICENSE) file.
