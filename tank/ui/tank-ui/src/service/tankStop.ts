import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const tankStop = (): Promise<AxiosResponse<void>> => {
    return axios.get(API_ROOT + '/tank/stop')
}