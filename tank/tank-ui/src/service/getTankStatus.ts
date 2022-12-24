import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";
import {TankStatus} from "../TankStatus";

export const getTankStatus = (): Promise<AxiosResponse<TankStatus>> => {
    return axios.get(API_ROOT + '/tank/status');
}