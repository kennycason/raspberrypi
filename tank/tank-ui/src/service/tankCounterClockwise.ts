import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const tankCounterClockwise = (): Promise<AxiosResponse<void>> => {
    return axios.get(API_ROOT + '/tank/counter-clockwise')
}