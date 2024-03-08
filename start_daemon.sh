#!/usr/bin/env bash

sudo systemctl daemon-reload
sudo systemctl enable atm_data_seeder.service
sudo systemctl start atm_data_seeder.service


sudo systemctl status atm_data_seeder.service