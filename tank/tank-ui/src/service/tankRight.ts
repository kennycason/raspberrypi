import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const tankRight = (): Promise<AxiosResponse<void>> => {
    return axios.get(API_ROOT + '/tank/turn-right')
}