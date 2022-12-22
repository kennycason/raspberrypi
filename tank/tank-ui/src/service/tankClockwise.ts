import axios, { AxiosResponse } from 'axios';
import { API_ROOT } from "../config";

export const tankClockwise = (): Promise<AxiosResponse<void>> => {
    return axios.get(API_ROOT + '/tank/clockwise')
}