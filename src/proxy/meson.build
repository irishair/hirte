# SPDX-License-Identifier: GPL-2.0-or-later
# proxy build configuration

proxy_src = [
  'main.c',
]

executable(
  'bluechi-proxy',
  proxy_src,
  dependencies: [
    systemd_dep,
  ],
  link_with: [
    bluechi_lib,
  ],
  c_args: common_cflags,
  include_directories: include_directories('..'),
  install: true
)
