# GCC Cross Compiler build script

`cxc-build` is a python script that builds a large collection of GCC cross compilers for various platforms.

## What is built

`GMP`, `MPFR`, and `MPC` are built only once as they are shared between all of the toolchains built by this script. `binutils`, `gdb`, `gcc`, and `newlib` are then built for each of the selected targets.

## Currently Supported Targets

| Triple                   | Builds             |
|--------------------------|--------------------|
| `aarch64-none-elf`       | :heavy_check_mark: |
| `aarch64-unknown-elf`    | :heavy_check_mark: |
| `arm-none-eabi`          | :heavy_check_mark: |
| `frv-none-elf`           | :heavy_check_mark: |
| `frv-unknown-elf`        | :heavy_check_mark: |
| `ia64-none-elf`          | :heavy_check_mark: |
| `ia64-unknown-elf`       | :heavy_check_mark: |
| `lm32-none-elf`          | :heavy_check_mark: |
| `lm32-unknown-elf`       | :heavy_check_mark: |
| `m68k-none-elf`          | :heavy_check_mark: |
| `m68k-unknown-elf`       | :heavy_check_mark: |
| `microblaze-none-elf`    | :heavy_check_mark: |
| `microblaze-unknown-elf` | :heavy_check_mark: |
| `mips-none-elf`          | :heavy_check_mark: |
| `mips-unknown-elf`       | :heavy_check_mark: |
| `or1k-none-elf`          | :heavy_check_mark: |
| `or1k-unknown-elf`       | :heavy_check_mark: |
| `ppc-none-elf`           | :heavy_check_mark: |
| `ppc-unknown-elf`        | :heavy_check_mark: |
| `ppcle-none-eabi`        | :heavy_check_mark: |
| `ppcle-none-elf`         | :heavy_check_mark: |
| `riscv32-none-elf`       | :heavy_check_mark: |
| `riscv32-unknown-elf`    | :heavy_check_mark: |
| `riscv64-none-elf`       | :heavy_check_mark: |
| `riscv64-unknown-elf`    | :heavy_check_mark: |
| `s390x-ibm-tpf`          | :heavy_check_mark: |
| `sparc64-none-elf`       | :heavy_check_mark: |
| `sparc64-unknown-elf`    | :heavy_check_mark: |
| `x86_64-none-elf`        | :heavy_check_mark: |
| `x86_64-unknown-elf`     | :heavy_check_mark: |

## TODO

There are a few things that need to be fixed or added. They are as follows.

 * Allow for selection of install and build paths at execution time without the need to edit the script
 * Allow for selection of targets to build and/or not build
 * Fix the `x-unknown-linux` targets so they build and then enable them
 * Add an `avr` target

## License

This script is licensed under the BSD 3 Clause, the full text of which can be found in the [`LICENSE`](./LICENSE) file.
